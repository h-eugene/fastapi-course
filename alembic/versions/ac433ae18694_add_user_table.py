"""add user table

Revision ID: ac433ae18694
Revises: 4e1175dd8b7e
Create Date: 2024-11-09 20:08:27.561466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac433ae18694'
down_revision: Union[str, None] = '4e1175dd8b7e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column("email", sa.String(),
                              nullable=False, unique=True),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False,
                              server_default=sa.text('now()')))

    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
