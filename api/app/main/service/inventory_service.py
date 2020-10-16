from app.main import db
from app.main.models import Inventory, Store, Product


def get_all_inventory():
    """"List all products from all stores"""
    return Inventory.query.all()


def get_store_inventory(branch_number):
    """"List all products from a store branch number"""
    return (
        Inventory.query.join(Store)
        .filter(
            Store.branch_number == branch_number,
        )
        .all()
    )


def get_store_sku_inventory(branch_number, sku):
    """List the number of pieces of a product available on a branch"""
    product = Product.query.filter_by(sku=sku).first()
    store = Store.query.filter_by(branch_number=branch_number).first()

    return Inventory.query.filter_by(
        product_id=product.id,
        store_id=store.id,
    ).first()


def save_new_inventory(data):
    """Save a product in a store"""
    product = Product.query.filter_by(sku=data["sku"]).first()
    store = Store.query.filter_by(branch_number=data["branch_number"]).first()

    inventory = Inventory.query.filter_by(
        product_id=product.id,
        store_id=store.id,
    ).first()

    if not inventory:
        new_inventory = Inventory(
            product_id=product.id,
            store_id=store.id,
            qty=data["qty"],
        )
        save_changes(new_inventory)
        response_object = {
            "status": "success",
            "message": "Successfully registered.",
        }
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "Inventory already exists.",
        }
        return response_object, 409


def update_inventory(data):
    """Updates the number of pieces of a product in a store"""
    product = Product.query.filter_by(sku=data["sku"]).first()
    store = Store.query.filter_by(branch_number=data["branch_number"]).first()

    inventory = Inventory.query.filter_by(
        product_id=product.id,
        store_id=store.id,
    ).first()

    if inventory:
        new_qty = inventory.qty + data["qty"]
        new_qty = new_qty if new_qty > 0 else 0
        inventory.qty = new_qty
        save_changes(inventory)

        response_object = {
            "status": "success",
            "message": "Successfully updated.",
        }
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "Inventory already exists.",
        }
        return response_object, 409


def inventory_store_sku_is_stockout(branch_number, sku):
    inventory = get_store_sku_inventory(branch_number, sku)
    stockout = False if inventory.qty > 0 else True
    return {"is_stockout": stockout}


def save_changes(data):
    db.session.add(data)
    db.session.commit()
