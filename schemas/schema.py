from pydantic import BaseModel
# from typing import Optional
# validation
# optional[int]

# support price have three fields
class SupportPrice(BaseModel):

    id: int
    name: str
    price: float


# support category have three fields
class SupportCategory(BaseModel):
    id: int
    name: str
    support_price: int

# support purpose have three fields
class SupportPurpose(BaseModel):
    id: int
    name: str
    support_category: int









