"""add url to course

Revision ID: 6d6cc1abcaa7
Revises: 49cc18d54730
Create Date: 2024-05-24 16:25:09.889071

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '6d6cc1abcaa7'
down_revision: Union[str, None] = '49cc18d54730'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('course', 'description',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=mysql.TEXT(),
               existing_nullable=False)
    op.drop_column('course', 'url')
    # ### end Alembic commands ###