"""init

Revision ID: 26c3d2c3e095
Revises: bb4d0246887a
Create Date: 2025-03-19 22:38:10.400318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26c3d2c3e095'
down_revision: Union[str, None] = 'bb4d0246887a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
