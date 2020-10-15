from flask_restplus import Api
from flask import Blueprint

from app.main.controller.product_controller import api as product_ns
from app.main.controller.store_controller import api as store_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="FLASK VIRTUAL INVENTORY WEB SERVICE",
    version="1.0",
    description="Virtual inventory system with Flask restplus web service",
)

api.add_namespace(product_ns, path="/product")
api.add_namespace(store_ns, path="/store")
