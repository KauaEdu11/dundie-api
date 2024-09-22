"""ensure_admin_user

Revision ID: 83204136be00
Revises: e1fd7590e2cf
Create Date: 2024-09-22 13:51:49.509332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

from dundie.models.user import User
from sqlmodel import Session

# revision identifiers, used by Alembic.
revision: str = '83204136be00'
down_revision: Union[str, None] = 'e1fd7590e2cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    admin = User(
        name="Admin",
        username="admin",
        email="admin@dm.com",
        dept="management",
        password="admin", # envvar/secrets - colocar password em settings
        currency="USD"
    )

    try:
        session.add(admin)
        session.commit()
    except sa.exc.IntegrityError:
        session.rollback()

def downgrade() -> None:
    pass
