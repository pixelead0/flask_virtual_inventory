from app.main import db

from app.main.models import TimestampMixin


class Product(db.Model, TimestampMixin):
    """
    Product information
    """

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    sku = db.Column(
        db.String(30),
        unique=True,
    )

    name = db.Column(
        db.String(100),
    )

    description = db.Column(
        db.String(200),
    )
