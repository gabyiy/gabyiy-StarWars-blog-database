"""empty message

Revision ID: fc74d2274aa4
Revises: 428e4dda4cee
Create Date: 2021-08-21 08:26:11.406983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc74d2274aa4'
down_revision = '428e4dda4cee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorite', sa.Column('people_id', sa.Integer(), nullable=True))
    op.add_column('favorite', sa.Column('planet_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'favorite', 'planet', ['planet_id'], ['id'])
    op.create_foreign_key(None, 'favorite', 'people', ['people_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'favorite', type_='foreignkey')
    op.drop_constraint(None, 'favorite', type_='foreignkey')
    op.drop_column('favorite', 'planet_id')
    op.drop_column('favorite', 'people_id')
    # ### end Alembic commands ###
