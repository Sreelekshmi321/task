
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError
from config.db import conn
from models.index import support_price,support_purpose,support_category
from schemas.index import SupportCategory,SupportPrice,SupportPurpose
from sqlalchemy import select

support_data = APIRouter()

"""CRUD  SUPPORT PRICE-   """

# create
@support_data.post("/support-price/",response_model=SupportPrice)
async def create_support_price(data: SupportPrice):
    try:
        conn.execute(support_price.insert().values(name=data.name,price=data.price))
        return {"Support price created successfully"} ,status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT CREATED")

# update based on id
@support_data.put("/support-price/{id}",response_model=SupportPrice)
async def update_support_price(id:int,data: SupportPrice):
    try:
        conn.execute(support_price.update().where(support_price.id == id).values(name=data.name,price=data.price))
        return {"data update successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT UPDATED")

# delete based on id
@support_data.delete("/support-price/{id}",response_model=SupportPrice)
async def delete_support_price(id:int):
    try:
        conn.execute(support_price.delete().where(support_price.id == id))
        return {"Data deleted successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT DELETED")

# get specific id based details
@support_data.get("/support-price/{id}",response_model=SupportPrice)
async def get_support_price(id:int):
    try:
        conn.execute(select([support_price]).where(support_price.c.id == id)).fetchone()
        return {"Data fetched successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT GET")

# get all data
@support_data.get("/support-price/",response_model=SupportPrice)
async def get_all_support_price():
    try:
        conn.execute(support_price.get().select([support_price])).fetchall()
        return {"All data fetched successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT FETCHED")




"""#######   CRUD --- SUPPORT CATEGORY ########"""

# create new data
@support_data.post("/support-category/",response_model=SupportCategory)
async def create_support_category(data:SupportCategory):
    try:
        conn.execute(support_category.insert().values(name=data.name,support_price=data.support_price))
        return {"Support category created successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT CREATED")



# update data based on id
@support_data.put("/support_category/{id}",response_model=SupportCategory)
async def update_support_category(id:int,data: SupportCategory):
    try:
        conn.execute(support_price.update().where(support_category.id == id).values(name=data.name,price=data.support_price))
        return {"data update successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT UPDATED")



# delete data based on id
@support_data.delete("/support-category/{id}",response_model=SupportCategory)
async def delete_support_category(id:int):
    try:
        conn.execute(support_category.delete().where(support_price.id == id))
        return {"Data deleted successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT DELETED")



# get specified id based data
@support_data.get("/support-category/{id}",response_model=SupportCategory)
async def get_support_category(id:int):
    try:
        conn.execute(select([support_category]).where(support_category.c.id == id)).fetchone()
        return {"Data fetched successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT GET")



# get all data
@support_data.get("/support-category/",response_model=SupportPrice)
async def get_all_support_category():
    try:
        conn.execute(support_category.get().select([support_category])).fetchall()
        return {"All data fetched successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT FETCHED")



"""CRUD    SUPPORT PURPOSE    """

# create new data
@support_data.post("/support-purpose/",response_model=SupportPurpose)
async def create_support_price(data:SupportPurpose):
    try:
        conn.execute(support_purpose.insert().values(name=data.name,category=data.support_category))
        return {"Support price created successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT CREATED")



# update data based on id
@support_data.put("/support-purpose/{id}",response_model=SupportPurpose)
async def update_support_purpose(id:int,data: SupportPurpose):
    try:
        conn.execute(support_purpose.update().where(support_purpose.id == id).values(name=data.name,category=data.support_category))
        return {"data update successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT UPDATED")


# delete data based on id

@support_data.delete("/support-purpose/{id}",response_model=SupportPurpose)
async def delete_support_price(id:int):
    try:
        conn.execute(support_purpose.delete().where(support_purpose.id == id))
        return {"Data deleted successfully"}.status.HTTP_201_CREATED
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT DELETED")



# get specific data based on id
@support_data.get("/support-purpose/{id}",response_model=SupportPurpose)
async def get_support_category(id:int):
    try:
        conn.execute(select([support_purpose]).where(support_purpose.id == id)).fetchone()
        return {"Data fetched successfully"}
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT GET")


# get all data
@support_data.get("/support-purpose/",response_model=SupportPurpose)
async def get_all_support_category():
    try:
        conn.execute(support_purpose.get().select([support_purpose])).fetchall()
        return {"All data fetched successfully"}
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT FETCHED")


