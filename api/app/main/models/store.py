from app.main import db

from app.main.models import AddressMixin, TimestampMixin


class Store(db.Model, AddressMixin, TimestampMixin):
    """
    Store information
    """

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    branch_number = db.Column(
        db.Integer,
        unique=True,
    )

    name = db.Column(
        db.String(100),
    )

    description = db.Column(
        db.String(200),
    )
