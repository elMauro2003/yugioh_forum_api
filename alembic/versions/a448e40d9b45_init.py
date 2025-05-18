"""init

Revision ID: a448e40d9b45
Revises: e6f3d68d91e9
Create Date: 2025-05-04 00:25:39.335469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a448e40d9b45'
down_revision: Union[str, None] = 'e6f3d68d91e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
