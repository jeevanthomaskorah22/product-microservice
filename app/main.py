from fastapi import FastAPI
from . import models
from .database import engine
from .routers import product

models.Base.metadata.create_all(engine)
app=FastAPI(title='product-service')

app.include_router(product.router)

