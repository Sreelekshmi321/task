
from sqlalchemy import Table ,Column ,ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String ,Float ,Boolean
# from sqlalchemy.orm import relationship
from config.db import meta
from config.db import get_db


# table creation-support price
support_price = Table(
    'support_price' ,meta,

    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('name',String(255)),
    Column('price',Float),
    Column('description',String(255)))

# table creation-support category
support_category = Table(
    'support_category', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255)),
    Column('description',String(255)),
    Column('active',Boolean)
)

# table creation- category-price
category_price = Table(
    'category_price', meta,
    Column('category_id', Integer, ForeignKey('support_category.id'), primary_key=True),
    Column('price_id', Integer, ForeignKey('support_price.id'), primary_key=True)
)

# Support Purpose model
support_purpose = Table(
    'support_purpose',meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255)),
    Column('description',String(255))
)
# table creation- purpose_category
purpose_category = Table(
    'purpose_category', meta,
    Column('purpose_id', Integer, ForeignKey('support_purpose.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('support_category.id'), primary_key=True)
)



