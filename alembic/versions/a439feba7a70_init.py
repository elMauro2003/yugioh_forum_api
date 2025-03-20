"""init

Revision ID: a439feba7a70
Revises: 66bbdbaa25ef
Create Date: 2025-03-20 01:18:34.353973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a439feba7a70'
down_revision: Union[str, None] = '66bbdbaa25ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
