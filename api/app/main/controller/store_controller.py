from flask import request
from flask_restplus import Resource

from app.main.util.dto import StoreDto
from app.main.service.store_service import (
    save_new_store,
    get_all_stores,
    get_a_store,
)

api = StoreDto.api
_store = StoreDto.store


@api.route("/")
class StoreList(Resource):
    @api.doc("list_of_stores")
    @api.marshal_list_with(_store, envelope="data")
    def get(self):
        """List all stores"""
        return get_all_stores()

    @api.response(201, "Store successfully created.")
    @api.doc("create a new store")
    @api.expect(_store, validate=True)
    def post(self):
        """Creates a new Store """
        data = request.json
        return save_new_store(data=data)


@api.route("/<branch_number>")
@api.param("branch_number", "The Store branh number")
@api.response(404, "Store not found.")
class Store(Resource):
    @api.doc("get a store")
    @api.marshal_with(_store)
    def get(self, branch_number):
        """get a store given its branch number"""
        store = get_a_store(branch_number)
        if not store:
            api.abort(404)
        else:
            return store
