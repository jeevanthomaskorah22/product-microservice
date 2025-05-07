from .database import Base
from sqlalchemy import Column, Integer, String,Float


class Product(Base):
    __tablename__='Product'
    
    id = Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    price=Column(Float,nullable=False)