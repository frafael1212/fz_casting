"""empty message

Revision ID: eb71712fe7c9
Revises: 
Create Date: 2020-05-21 23:24:14.431640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb71712fe7c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actors', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('actors', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('movies', sa.Column('rdate', sa.String(), nullable=True))
    op.drop_column('movies', 'actor')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('actor', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('movies', 'rdate')
    op.drop_column('actors', 'gender')
    op.drop_column('actors', 'age')
    # ### end Alembic commands ###
