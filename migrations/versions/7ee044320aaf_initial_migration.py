"""Initial Migration

Revision ID: 7ee044320aaf
Revises: 
Create Date: 2020-09-21 21:11:45.778527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ee044320aaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('market', sa.String(length=255), nullable=True),
    sa.Column('product_info', sa.Text(), nullable=True),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    # ### end Alembic commands ###
