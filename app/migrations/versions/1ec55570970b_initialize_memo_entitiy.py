"""Initialize memo entitiy..

Revision ID: 1ec55570970b
Revises: 
Create Date: 2022-08-10 10:46:40.294035

"""
from alembic import op
import sqlalchemy as sa
import time


# revision identifiers, used by Alembic.
revision = '1ec55570970b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('memos'+str(time.time()),
    sa.Column('id', sa.String(length=120), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('content',sa.Text(), nullable=False),
    sa.Column('is_favorite', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_memo_title'),'memos',['title'],unique=False)



def downgrade() -> None:
    op.drop_index(op.f('ix_memo_title'), table_name='memos')
    op.drop_table('memos')
