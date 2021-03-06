"""empty message

Revision ID: 3681969f406e
Revises: db45dfdcaaf8
Create Date: 2021-07-10 13:20:16.263085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3681969f406e'
down_revision = 'db45dfdcaaf8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 's_category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('s_category', sa.VARCHAR(length=30), nullable=False))
    # ### end Alembic commands ###
