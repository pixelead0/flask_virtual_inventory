from app.main import db
from app.main.models import Product


def save_new_product(data):
    product = Product.query.filter_by(sku=data["sku"]).first()
    if not product:
        new_product = Product(
            sku=data["sku"],
            name=data["name"],
            description=data["description"],
        )
        save_changes(new_product)
        response_object = {
            "status": "success",
            "message": "Successfully registered.",
        }
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "Product already exists.",
        }
        return response_object, 409


def get_all_products():
    return Product.query.all()


def get_a_product(sku):
    return Product.query.filter_by(sku=sku).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
