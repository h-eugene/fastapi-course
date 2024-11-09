"""add content column to post table

Revision ID: 4e1175dd8b7e
Revises: e5e23289bac3
Create Date: 2024-11-09 16:32:48.266484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e1175dd8b7e'
down_revision: Union[str, None] = 'e5e23289bac3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
