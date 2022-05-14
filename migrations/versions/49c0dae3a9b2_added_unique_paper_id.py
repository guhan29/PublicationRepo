"""added unique paper id

Revision ID: 49c0dae3a9b2
Revises: 85b62fa0e490
Create Date: 2022-04-24 16:56:42.589356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49c0dae3a9b2'
down_revision = '85b62fa0e490'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publish_paper', sa.Column('unique_paper_id', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('publish_paper', 'unique_paper_id')
    # ### end Alembic commands ###