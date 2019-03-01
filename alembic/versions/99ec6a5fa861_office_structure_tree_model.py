"""office structure tree model

Revision ID: 99ec6a5fa861
Revises: ee5c60d6b79c
Create Date: 2019-03-01 15:39:09.278467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99ec6a5fa861'
down_revision = 'ee5c60d6b79c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('structure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('lft', sa.Integer(), nullable=False),
    sa.Column('rgt', sa.Integer(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('tree_id', sa.Integer(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['structure.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_structure_name'), 'structure', ['name'], unique=True)
    op.create_index('structure_level_idx', 'structure', ['level'], unique=False)
    op.create_index('structure_lft_idx', 'structure', ['lft'], unique=False)
    op.create_index('structure_rgt_idx', 'structure', ['rgt'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('structure_rgt_idx', table_name='structure')
    op.drop_index('structure_lft_idx', table_name='structure')
    op.drop_index('structure_level_idx', table_name='structure')
    op.drop_index(op.f('ix_structure_name'), table_name='structure')
    op.drop_table('structure')
    # ### end Alembic commands ###