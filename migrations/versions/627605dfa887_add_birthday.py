"""add birthday

Revision ID: 627605dfa887
Revises: 7a94609193b6
Create Date: 2022-05-31 18:40:46.156910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '627605dfa887'
down_revision = '7a94609193b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('birthday', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'birthday')
    # ### end Alembic commands ###
