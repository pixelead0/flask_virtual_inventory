from flask_restplus import Api
from flask import Blueprint

from app.main.controller.product_controller import api as product_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="FLASK VIRTUAL INVENTORY WEB SERVICE",
    version="1.0",
    description="Virtual inventory system with Flask restplus web service",
)

api.add_namespace(product_ns, path="/product")
