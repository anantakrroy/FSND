"""empty message

Revision ID: 9aeef676f08e
Revises: 49f3263a9416
Create Date: 2021-04-29 11:08:18.519290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aeef676f08e'
down_revision = '49f3263a9416'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show', 'start_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('start_time', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
