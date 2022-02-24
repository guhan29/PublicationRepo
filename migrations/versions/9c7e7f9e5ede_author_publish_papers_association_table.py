"""author_publish_papers association table

Revision ID: 9c7e7f9e5ede
Revises: 2cc351062533
Create Date: 2022-02-24 22:17:24.137874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c7e7f9e5ede'
down_revision = '2cc351062533'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author_publish_papers',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('publish_paper_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['publish_paper_id'], ['publish_paper.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'publish_paper_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('author_publish_papers')
    # ### end Alembic commands ###