"""init

Revision ID: 66bbdbaa25ef
Revises: 26c3d2c3e095
Create Date: 2025-03-20 01:15:37.918439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66bbdbaa25ef'
down_revision: Union[str, None] = '26c3d2c3e095'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
