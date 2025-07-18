"""new fields in user model

Revision ID: 96aab37f7e20
Revises: 98afe108cd20
Create Date: 2025-06-23 18:36:23.356335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96aab37f7e20'
down_revision = '98afe108cd20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
