"""add a few last columns to posts table

Revision ID: b07675c58301
Revises: bdd352101a8e
Create Date: 2024-11-09 20:39:59.075696

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b07675c58301'
down_revision: Union[str, None] = 'bdd352101a8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        "published", sa.Boolean(), server_default="TRUE", nullable=False))
    op.add_column('posts', sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=False,
        server_default=sa.text('NOW()')))

    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
