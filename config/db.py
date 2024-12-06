"""DATABASE CONNECTION"""


from sqlalchemy import create_engine ,MetaData

# engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/TASK")
# engine = create_engine("postgresql://postgres:1234@localhost:5432/ASSESSMENT")
# database details
engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/ASSESSMENT")

meta=MetaData()
# onnection to the database
conn=engine.connect()



