"""init

Revision ID: 3dfb4da0e336
Revises: 
Create Date: 2022-04-30 21:29:45.414271

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3dfb4da0e336'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('statistics')


def downgrade():
    op.create_table('statistics',
                    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
                    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True),
                    sa.Column('views', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('clicks', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('cost', sa.REAL(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='statistics_pkey')
                    )
