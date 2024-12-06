# """DATABASE CONNECTION"""


# meta=MetaData()
# # onnection to the database
# conn=engine.connect()


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/ASSESSMENT1"



engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

meta = MetaData()  # Initialize MetaData here

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



