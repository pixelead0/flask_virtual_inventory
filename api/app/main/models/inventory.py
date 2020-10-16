from app.main import db

from app.main.models import TimestampMixin
from sqlalchemy.ext.hybrid import hybrid_property
from app.main.models import Store, Product


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

    qty = db.Column(
        db.Integer,
        default=0,
    )

    __table_args__ = (
        db.UniqueConstraint(
            "store_id",
            "product_id",
        ),
    )

    @hybrid_property
    def branch_number(self):
        store = Store.query.filter_by(id=self.store_id).first()
        return store.branch_number

    @hybrid_property
    def sku(self):
        product = Product.query.filter_by(id=self.product_id).first()
        return product.sku
