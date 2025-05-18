"""init

Revision ID: d3a29f797014
Revises: a448e40d9b45
Create Date: 2025-05-04 00:26:34.754681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3a29f797014'
down_revision: Union[str, None] = 'a448e40d9b45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
