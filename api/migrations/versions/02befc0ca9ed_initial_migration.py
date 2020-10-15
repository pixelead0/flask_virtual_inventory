"""initial migration

Revision ID: 02befc0ca9ed
Revises: 
Create Date: 2020-10-14 19:29:22.216450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02befc0ca9ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sku', sa.String(length=30), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sku')
    )
    op.create_table('store',
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('address_street', sa.String(length=100), nullable=True),
    sa.Column('address_number', sa.String(length=20), nullable=True),
    sa.Column('address_indoor_number', sa.String(length=20), nullable=True),
    sa.Column('address_zipcode', sa.String(length=5), nullable=True),
    sa.Column('address_suburb', sa.String(length=100), nullable=True),
    sa.Column('address_municipality', sa.String(length=100), nullable=True),
    sa.Column('address_state', sa.String(length=100), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory',
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('store_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inventory')
    op.drop_table('store')
    op.drop_table('product')
    # ### end Alembic commands ###
