"""init

Revision ID: bb4d0246887a
Revises: e558a5042449
Create Date: 2025-03-19 20:13:03.181658

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb4d0246887a'
down_revision: Union[str, None] = 'e558a5042449'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
