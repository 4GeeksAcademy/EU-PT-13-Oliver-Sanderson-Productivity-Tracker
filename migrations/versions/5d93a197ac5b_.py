"""empty message

Revision ID: 5d93a197ac5b
Revises: a92458e5b493
Create Date: 2023-10-26 08:08:33.463457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d93a197ac5b'
down_revision = 'a92458e5b493'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('session', schema=None) as batch_op:
        batch_op.add_column(sa.Column('work_time_secs', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('fun_time_secs', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('session', schema=None) as batch_op:
        batch_op.drop_column('fun_time_secs')
        batch_op.drop_column('work_time_secs')

    # ### end Alembic commands ###