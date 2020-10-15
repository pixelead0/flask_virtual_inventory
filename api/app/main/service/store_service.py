from app.main import db
from app.main.models import Store


def save_new_store(data):
    """Save store information"""
    store = Store.query.filter_by(branch_number=data["branch_number"]).first()
    if not store:
        new_store = Store(
            branch_number=data["branch_number"],
            name=data["name"],
            description=data["description"],
            address_street=data["address_street"],
            address_number=data["address_number"],
            address_indoor_number=data["address_indoor_number"],
            address_zipcode=data["address_zipcode"],
            address_suburb=data["address_suburb"],
            address_municipality=data["address_municipality"],
            address_state=data["address_state"],
        )
        save_changes(new_store)
        response_object = {
            "status": "success",
            "message": "Successfully registered.",
        }
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "Store already exists.",
        }
        return response_object, 409


def get_all_stores():
    """List all stores"""
    return Store.query.all()


def get_a_store(branch_number):
    """Get store information by branch number"""
    return Store.query.filter_by(branch_number=branch_number).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
