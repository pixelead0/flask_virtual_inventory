from flask import request
from flask_restplus import Resource

from app.main.util.dto import InventoryDto
from app.main.service import inventory_service

api = InventoryDto.api
_inventory = InventoryDto.inventory
_inventory_stockout = InventoryDto.inventory_stockout


@api.route("/")
class InventoryList(Resource):
    @api.doc("list_of_inventory")
    @api.marshal_list_with(_inventory, envelope="data")
    def get(self):
        """List all inventory"""
        return inventory_service.get_all_inventory()

    @api.response(201, "Inventory successfully created.")
    @api.doc("create a new inventory of a sku in a store")
    @api.expect(_inventory, validate=True)
    def post(self):
        """Creates a new Inventory """
        data = request.json
        return inventory_service.save_new_inventory(data=data)

    @api.response(201, "Inventory successfully updated.")
    @api.doc("Updates the number of pieces of a product in a store")
    @api.expect(_inventory, validate=True)
    def put(self):
        """Updates the number of pieces of a product in a store"""
        data = request.json
        return inventory_service.update_inventory(data=data)


@api.route("/<branch_number>")
@api.param("branch_number", "The store branch number")
class InventoryStoreList(Resource):
    @api.doc("list_of_inventory_in_store")
    @api.marshal_list_with(_inventory, envelope="data")
    def get(self, branch_number):
        """Inventory list in a store"""
        return inventory_service.get_store_inventory(branch_number)


@api.route("/<branch_number>/sku/<sku>")
@api.param("branch_number", "The store branch number")
@api.param("sku", "The product sku")
class InventoryStoreSkuList(Resource):
    @api.doc("inventory_of_a_sku_in_store")
    @api.marshal_list_with(_inventory, envelope="data")
    def get(self, branch_number, sku):
        """List the inventory of a sku in this store"""
        return inventory_service.get_store_sku_inventory(branch_number, sku)


@api.route("/<branch_number>/sku/<sku>/stockout")
@api.param("branch_number", "The store branch number")
@api.param("sku", "The product sku")
@api.response(404, "SKU not found in this store.")
class InventoryStoreSkuStockout(Resource):
    @api.doc("Check if a product is in stockout")
    @api.marshal_with(_inventory_stockout)
    def get(self, branch_number, sku):
        """get a inventory given its branch number"""
        inventory = inventory_service.inventory_store_sku_is_stockout(
            branch_number,
            sku,
        )
        if not inventory:
            api.abort(404)
        else:
            return inventory
