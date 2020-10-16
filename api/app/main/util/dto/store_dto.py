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
            "address_street": fields.String(
                required=False,
                description="store address street",
            ),
            "address_number": fields.String(
                required=False,
                description="store address number",
            ),
            "address_indoor_number": fields.String(
                required=False,
                description="store address indoor number",
            ),
            "address_zipcode": fields.String(
                required=False,
                max_length=5,
                description="store address zipcode",
            ),
            "address_suburb": fields.String(
                required=False,
                description="store address suburb",
            ),
            "address_municipality": fields.String(
                required=False,
                description="store address municipality",
            ),
            "address_state": fields.String(
                required=False,
                description="store address state",
            ),
        },
    )
