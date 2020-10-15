from app.main import db

from app.main.models import TimestampMixin


class Inventory(db.Model, TimestampMixin):
    """
    Inventory information
    """

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.id"),
    )

    store_id = db.Column(
        db.Integer,
        db.ForeignKey("store.id"),
    )

    __table_args__ = (
        db.UniqueConstraint(
            "store_id",
            "product_id",
            # name="_store_product_ix",
        ),
    )
