from flask_restplus import Namespace, fields


class ProductDto:
    api = Namespace("product", description="product information")
    product = api.model(
        "product",
        {
            "sku": fields.String(
                required=True,
                description="product SKU",
            ),
            "name": fields.String(
                required=True,
                description="product name",
            ),
            "description": fields.String(
                required=True,
                description="product description",
            ),
            "id": fields.Integer(
                description="product identifier",
            ),
        },
    )
