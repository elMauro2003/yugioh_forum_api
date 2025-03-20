"""init

Revision ID: 3d330e705c89
Revises: a439feba7a70
Create Date: 2025-03-20 01:20:06.126234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d330e705c89'
down_revision: Union[str, None] = 'a439feba7a70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
