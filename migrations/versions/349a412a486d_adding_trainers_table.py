"""adding trainers table

Revision ID: 349a412a486d
Revises: 
Create Date: 2023-09-27 08:43:10.316480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '349a412a486d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trainers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pc_name', sa.String(), nullable=False),
    sa.Column('hometown', sa.String(), nullable=True),
    sa.Column('pc_password_hash', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pc_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trainers')
    # ### end Alembic commands ###
