from flask_restplus import Namespace, fields


class InventoryDto:
    api = Namespace("inventory", description="inventory information")
    inventory = api.model(
        "inventory",
        {
            "sku": fields.String(
                required=True,
                description="product SKU",
            ),
            "branch_number": fields.Integer(
                required=True,
                description="store branch number",
            ),
            "qty": fields.Integer(
                required=True,
                description="Units for this product on branch numner",
            ),

        },
    )

    inventory_stockout = api.model(
        "inventory_stockout",
        {
            "is_stockout": fields.Boolean(
                description="Check if a product is in stockout",
            ),

        },
    )
