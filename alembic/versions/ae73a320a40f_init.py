"""init

Revision ID: ae73a320a40f
Revises: 5bc88c20f04e
Create Date: 2025-05-03 16:58:43.267234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae73a320a40f'
down_revision: Union[str, None] = '5bc88c20f04e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
