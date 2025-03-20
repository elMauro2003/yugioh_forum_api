"""init

Revision ID: 5bc88c20f04e
Revises: 3d330e705c89
Create Date: 2025-03-20 01:23:19.164819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bc88c20f04e'
down_revision: Union[str, None] = '3d330e705c89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
