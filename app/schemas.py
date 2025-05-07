from typing import List
from pydantic import BaseModel 

class Product(BaseModel):
    name: str
    price: float
    
    
class ShowProduct(BaseModel):
    name:str
    price:float
    class Config():#since sqlalchemy uses orm
        orm_mode=True