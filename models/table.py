from sqlalchemy import Table ,Column
from sqlalchemy.sql.sqltypes import Integer, String ,Float
# from sqlalchemy.orm import relationship
from config.db import meta

# table creation-support price
support_price = Table(
    'support_price' ,meta,
    Column('id',Integer,primary_key=True ,autoincrement=True ),
    Column('name',String(255)),
    Column('price',Float)

)

# table creation-support category
support_category = Table(
    'support_category', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255)),
    Column('support_price', Integer)
)

# table creation-supportpurpose
# Support Purpose model
support_purpose = Table(
    'support_purpose',meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255)),
    Column('support_category', Integer),
)
