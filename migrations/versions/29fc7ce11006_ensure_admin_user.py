"""ensure_admin_user

Revision ID: 29fc7ce11006
Revises: 68e328658ef7
Create Date: 2024-04-04 23:05:47.975381

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel

from dundie.models.user import User  # NEW
from sqlmodel import Session  # NEW

# revision identifiers, used by Alembic.
revision = '29fc7ce11006'
down_revision = '68e328658ef7'
branch_labels = None
depends_on = None


def upgrade() -> None:  # NEW
    bind = op.get_bind()
    session = Session(bind=bind)

    admin = User(
        name="Admin",
        username="admin",
        email="admin@dm.com",
        dept="management",
        currency="USD",
        password="admin",  # pyright: ignore
    )
    # if admin user already exists it will raise IntegrityError
    try:
        session.add(admin)
        session.commit()
    except sa.exc.IntegrityError:
        session.rollback()


def downgrade() -> None:
    pass
