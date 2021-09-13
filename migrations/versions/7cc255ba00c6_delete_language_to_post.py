"""delete language to post

Revision ID: 7cc255ba00c6
Revises: 9bf02b41760b
Create Date: 2021-09-09 18:47:31.166742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cc255ba00c6'
down_revision = '9bf02b41760b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.VARCHAR(length=5), nullable=True))
    # ### end Alembic commands ###
