
from pydantic import BaseModel
from typing import List, Optional

class SupportPrice(BaseModel):
    name: str
    price: float
    description: str



class SupportCategory(BaseModel):
    id: int
    name: str
    description: str
    active: bool
    prices: List[SupportPrice] = []



class SupportPurpose(BaseModel):
    id: int
    name: str
    description: str
    categories: List[SupportCategory] = []


class CategoryPrice(BaseModel):
    price_id: int
    category_id: int


class PurposeCategory(BaseModel):
    category_id: int
    purpose_id:int






