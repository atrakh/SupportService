"""empty message

Revision ID: 58ef238c720e
Revises: 899a70e24bf3
Create Date: 2018-08-18 12:06:32.122274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58ef238c720e'
down_revision = '899a70e24bf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('set_path', sa.String(length=120), nullable=True))
    op.drop_index('ix_user_username', table_name='user')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.create_index('ix_user_username', 'user', ['username'], unique=True)
    op.drop_column('user', 'set_path')
    # ### end Alembic commands ###
