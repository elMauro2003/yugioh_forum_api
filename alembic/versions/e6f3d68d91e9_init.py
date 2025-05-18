"""init

Revision ID: e6f3d68d91e9
Revises: d3a62c70a8b8
Create Date: 2025-05-04 00:23:49.055106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6f3d68d91e9'
down_revision: Union[str, None] = 'd3a62c70a8b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
