from app.main import db

from datetime import datetime


class TimestampMixin(object):
    """
    Timestamp fields to know if a record is active
    and when it was created or modified
    """

    is_active = db.Column(
        db.Boolean,
        default=True,
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
