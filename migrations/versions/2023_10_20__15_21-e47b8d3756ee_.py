"""empty message

Revision ID: e47b8d3756ee
Revises: 96f168565284
Create Date: 2023-10-20 15:21:41.194778

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_file


# revision identifiers, used by Alembic.
revision: str = 'e47b8d3756ee'
down_revision: Union[str, None] = '96f168565284'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('photo', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'photo')
    # ### end Alembic commands ###
