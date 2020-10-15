from flask_restplus import Namespace, fields


class StoreDto:
    api = Namespace("store", description="store information")
    store = api.model(
        "store",
        {
            "branch_number": fields.Integer(
                required=True,
                description="store branch number",
            ),
            "name": fields.String(
                required=True,
                description="store SKU",
            ),
            "description": fields.String(
                required=True,
                description="store description",
            ),
            "street": fields.String(
                required=False,
                description="store street",
            ),
            "number": fields.String(
                required=False,
                description="store address number",
            ),
            "indoor_number": fields.String(
                required=False,
                description="store address indoor number",
            ),
            "zipcode": fields.String(
                required=False,
                description="store zipcode",
                max_length=5
            ),
            "suburb": fields.String(
                required=False,
                description="store suburb",
            ),
            "municipality": fields.String(
                required=False,
                description="store municipality",
            ),
            "state": fields.String(
                required=False,
                description="store state",
            ),
        },
    )
