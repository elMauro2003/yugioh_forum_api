"""init

Revision ID: 0af6364efe75
Revises: b6862163904a
Create Date: 2025-03-19 12:56:24.429423

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0af6364efe75'
down_revision: Union[str, None] = 'b6862163904a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
