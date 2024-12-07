
from fastapi import APIRouter, HTTPException, status,Depends
from sqlalchemy.exc import IntegrityError
from models.index import support_price,support_purpose,support_category,purpose_category,category_price
from schemas.index import SupportCategory,SupportPrice,SupportPurpose
from sqlalchemy import select
from sqlalchemy.orm import Session
from config.db import get_db

support_data = APIRouter()

# CRETAE SUPPORT PRICE
@support_data.post("/support-price/", response_model=SupportPrice)
async def create_support_price(data: SupportPrice, db: Session = Depends(get_db)):
    try:
        result = db.execute(support_price.insert().values(name=data.name, price=data.price, description=data.description))
        created_id = result.inserted_primary_key[0]
        # Return data
        return SupportPrice(id=created_id, name=data.name, price=data.price, description=data.description)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not created")
    except Exception:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid data")


# UPDATE SUPPORT PRICE
@support_data.put("/support-price/{id}", response_model=SupportPrice)
async def update_support_price(id: int, data: SupportPrice, db: Session = Depends(get_db)):
    try:
        existing_price = db.execute(support_price.select().where(support_price.c.id == id)).fetchone()
        if not existing_price:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Price not found")

        db.execute(support_price.update().where(support_price.c.id == id).values(name=data.name, price=data.price, description=data.description))
        return SupportPrice(id=id, name=data.name, price=data.price, description=data.description), status.HTTP_200_OK
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not updated")


# DELETE SUPPORT PRICE
@support_data.delete("/support-price/{id}", response_model=SupportPrice)
async def delete_support_price(id: int, db: Session = Depends(get_db)):
    try:
        price = db.execute(support_price.select().where(support_price.c.id == id)).fetchone()
        if not price:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Support price not found")

        db.execute(support_price.delete().where(support_price.c.id == id))
        return {"message": "Data deleted successfully"}, status.HTTP_200_OK
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Support price not deleted")



# GET DATA BASED ON ID
@support_data.get("/support-price/{id}", response_model=SupportPrice)
async def get_support_price(id: int, db: Session = Depends(get_db)):
    try:
        result = db.execute(support_price.select().where(support_price.c.id == id)).fetchone()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not have data")
        return result
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not have data")


# GET ALL DATA
@support_data.get("/support-price/", response_model=SupportPrice)
async def get_all_support_price(db: Session = Depends(get_db)):
    try:
        result = db.execute(support_price.select()).fetchall()
        return result
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not get data")



"""CRUD for Support Category   ,price assign category  ,  and category assign purpose"""

# create support category

@support_data.post("/support-category/", response_model=SupportCategory)
async def create_support_category(data: SupportCategory, db: Session = Depends(get_db)):
    try:
        result = db.execute(support_category.insert().values(name=data.name, description=data.description, active=data.active))
        created_id = result.inserted_primary_key[0]
        return SupportCategory(id=created_id, name=data.name, description=data.description, active=data.active)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="category not created")


"""   ######################################               ASSIGN PRICE TO CATEGORY               #################################"""

@support_data.post("/support-category/{category_id}/support-price/{price_id}")
async def price_to_category(category_id: int, price_id: int, db: Session = Depends(get_db)):
    category = db.query(support_category).filter(support_category.c.id == category_id).first()
    price = db.query(support_price).filter(support_price.c.id == price_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    db.execute(category_price.insert().values(category_id=category_id, price_id=price_id))
    db.commit()
    return {"message": "Price assigned to category"}



# UPDATE PRICE TO CATEGORY
@support_data.put("/support-category/{category_id}/support-price/{price_id}")

async def update_price_to_category(category_id: int, price_id: int, db: Session = Depends(get_db)):
    category = db.query(support_category).filter(support_category.c.id == category_id).first()
    price = db.query(support_price).filter(support_price.c.id == price_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    old_data=db.query(category_price).filter(support_category.c.id==category_id ,support_price.c.id == price_id).first()

    if old_data:

        raise HTTPException(status_code=400, detail="already exist price in category")

    db.execute(category_price.insert().values(category_id=category_id, price_id=price_id))
    db.commit()
    return {"message": "Price assigned to category"}



# crud for support_purpose


@support_data.post("/support-purpose/", response_model=SupportPurpose)
async def create_support_purpose(data: SupportCategory, db: Session = Depends(get_db)):
    try:
        result = db.execute(support_purpose.insert().values(name=data.name, description=data.description))
        created_id = result.inserted_primary_key[0]
        return SupportPurpose(id=created_id, name=data.name, description=data.description)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Purpose not created")


# ASSIGN category TO purpose
@support_data.post("/purposes/{purpose_id}/categories/{category_id}/")
async def category_to_purpose(purpose_id: int, category_id: int, db: Session = Depends(get_db)):
    purpose = db.query(support_purpose).filter(support_purpose.c.id == purpose_id).first()
    category = db.query(support_category).filter(support_category.c.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if not purpose:
        raise HTTPException(status_code=404, detail="Purpose not found")

    if not category.active:
        raise HTTPException(status_code=400, detail="category is not active")
    db.execute(purpose_category.insert().values(purpose_id=purpose_id, category_id=category_id))
    db.commit()
    return {"message": "Category assigned to purpose"}




# UPDATE category TO purpose
@support_data.put("/purposes/{purpose_id}/categories/{category_id}/")
async def update_category_to_purpose(purpose_id: int, category_id: int, db: Session = Depends(get_db)):
    purpose = db.query(support_purpose).filter(support_purpose.c.id == purpose_id).first()
    category = db.query(support_category).filter(support_category.c.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if not purpose:
        raise HTTPException(status_code=404, detail="Purpose not found")

    if not category.active:
        raise HTTPException(status_code=400, detail="category is not active")

    old_data=db.query(purpose_category).filter(support_category.c.id==category_id ,support_purpose.c.id == purpose_id).first()

    if old_data:

        raise HTTPException(status_code=400, detail="already exist price in category")
    db.execute(purpose_category.insert().values(purpose_id=purpose_id, category_id=category_id))
    db.commit()
    return {"message": "Category  updatedto purpose"}


# GET category TO purpose DATA BASED ON ID
@support_data.get("/purposes/{purpose_id}}/", response_model=PurposeCategory)
async def get_support_purpose(id: int, db: Session = Depends(get_db)):
    query = (
        db.query(purpose_category.c.purpose_id,purpose_category.c.category_id,support_category.c.name.label("category_name"),support_purpose.c.name.label("purpose_name"),)
        .join(support_category, purpose_category.c.category_id == support_category.c.id)
        .join(support_purpose, purpose_category.c.purpose_id == support_purpose.c.id)
        .filter(purpose_category.c.purpose_id == id)
    )

    result = query.all()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not have data")

    return [PurposeCategory(purpose_id=row.purpose_id,category_id=row.category_id,category_name=row.category_name,purpose_name=row.purpose_name, )for row in result
]








