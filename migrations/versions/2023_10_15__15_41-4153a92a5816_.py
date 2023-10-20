"""empty message

Revision ID: 4153a92a5816
Revises: b60f8554deb0
Create Date: 2023-10-15 15:41:39.168567

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_file
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4153a92a5816'
down_revision: Union[str, None] = 'b60f8554deb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('file', postgresql.JSONB(astext_type=sa.Text()), nullable=False))
    op.drop_column('file', 'name')
    op.drop_column('file', 'number')
    op.drop_column('file', 'info')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('info', sa.VARCHAR(length=16), autoincrement=False, nullable=False))
    op.add_column('file', sa.Column('number', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('file', sa.Column('name', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False))
    op.drop_column('file', 'file')
    # ### end Alembic commands ###
