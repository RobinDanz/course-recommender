"""add description to course

Revision ID: 49cc18d54730
Revises: 7093f96d03b0
Create Date: 2024-05-24 15:57:07.064865

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '49cc18d54730'
down_revision: Union[str, None] = '7093f96d03b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('description', sqlmodel.TEXT, nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'description')
    # ### end Alembic commands ###
