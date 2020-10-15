from app.main import db


class AddressMixin(object):
    """
    Address fields for use in other tables e.g. for deliveries
    """

    address_street = db.Column(db.String(100))
    address_number = db.Column(db.String(20))
    address_indoor_number = db.Column(db.String(20))
    address_zipcode = db.Column(db.String(5))
    address_suburb = db.Column(db.String(100))
    address_municipality = db.Column(db.String(100))
    address_state = db.Column(db.String(100))
