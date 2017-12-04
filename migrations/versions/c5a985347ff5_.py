"""empty message

Revision ID: c5a985347ff5
Revises: 1b966e7f4b9e
Create Date: 2017-12-03 22:08:53.268289

"""

# revision identifiers, used by Alembic.
revision = 'c5a985347ff5'
down_revision = '1b966e7f4b9e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
