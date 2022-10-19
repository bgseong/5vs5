"""Initialize nkmemo entity..

Revision ID: 91a766ee410f
Revises: 1ec55570970b
Create Date: 2022-08-10 11:10:33.132667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91a766ee410f'
down_revision = '1ec55570970b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('memos1660097290.484366')
    op.drop_index('ix_memo_title', table_name='memos')
    op.drop_index('ix_memos_title', table_name='memos')
    op.drop_table('memos')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('memos',
    sa.Column('id', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('is_favorite', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='memos_pkey')
    )
    op.create_index('ix_memos_title', 'memos', ['title'], unique=False)
    op.create_index('ix_memo_title', 'memos', ['title'], unique=False)
    op.create_table('memos1660097290.484366',
    sa.Column('id', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('is_favorite', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='memos1660097290.484366_pkey')
    )
    # ### end Alembic commands ###