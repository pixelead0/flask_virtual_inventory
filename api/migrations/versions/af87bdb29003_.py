"""empty message

Revision ID: af87bdb29003
Revises: 02befc0ca9ed
Create Date: 2020-10-15 06:08:25.629948

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'af87bdb29003'
down_revision = '02befc0ca9ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inventory')
    op.drop_table('product')
    op.drop_table('store')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('store',
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('address_street', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('address_number', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('address_indoor_number', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('address_zipcode', sa.VARCHAR(length=5), autoincrement=False, nullable=True),
    sa.Column('address_suburb', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('address_municipality', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('address_state', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('store_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='store_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('product',
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('product_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('sku', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='product_pkey'),
    sa.UniqueConstraint('sku', name='product_sku_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('inventory',
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('store_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='inventory_product_id_fkey'),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], name='inventory_store_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='inventory_pkey'),
    sa.UniqueConstraint('store_id', 'product_id', name='inventory_store_id_product_id_key')
    )
    # ### end Alembic commands ###