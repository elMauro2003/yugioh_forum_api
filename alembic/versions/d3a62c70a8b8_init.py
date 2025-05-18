"""init

Revision ID: d3a62c70a8b8
Revises: ae73a320a40f
Create Date: 2025-05-04 00:20:58.002317

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3a62c70a8b8'
down_revision: Union[str, None] = 'ae73a320a40f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
