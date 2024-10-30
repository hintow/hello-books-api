"""adds Book model

Revision ID: 684a2cf4ed7b
Revises: 
Create Date: 2024-10-25 00:27:05.453100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '684a2cf4ed7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
