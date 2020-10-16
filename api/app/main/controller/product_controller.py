from flask import request
from flask_restplus import Resource

from app.main.util.dto import ProductDto
from app.main.service.product_service import (
    save_new_product,
    get_all_products,
    get_a_product,
)

api = ProductDto.api
_product = ProductDto.product


@api.route("/")
class ProductList(Resource):
    @api.doc("list_of_products")
    @api.marshal_list_with(_product, envelope="data")
    def get(self):
        """List all products"""
        return get_all_products()

    @api.response(201, "Product successfully created.")
    @api.doc("create a new product")
    @api.expect(_product, validate=True)
    def post(self):
        """Creates a new Product """
        data = request.json
        return save_new_product(data=data)


@api.route("/<sku>")
@api.param("sku", "The Product SKU")
@api.response(404, "Product not found.")
class Product(Resource):
    @api.doc("get a product")
    @api.marshal_with(_product)
    def get(self, sku):
        """get a product given its SKU"""
        product = get_a_product(sku)
        if not product:
            api.abort(404)
        else:
            return product
