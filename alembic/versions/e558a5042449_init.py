"""init

Revision ID: e558a5042449
Revises: 0af6364efe75
Create Date: 2025-03-19 20:08:07.982747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e558a5042449'
down_revision: Union[str, None] = '0af6364efe75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
