"""empty message

Revision ID: 33600858f7d9
Revises: 58e9762d7ab6
Create Date: 2021-07-27 13:14:08.149173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33600858f7d9'
down_revision = '58e9762d7ab6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'hired_trucks', ['phone_no'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'hired_trucks', type_='unique')
    # ### end Alembic commands ###
