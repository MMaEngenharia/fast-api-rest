
from fastapi_users import models
from pydantic import BaseModel

class User(models.BaseUser):
    pass

class UserCreate(models.BaseUserCreate):
    pass

class UserUpdate(User, models.BaseUserUpdate):
    pass

class UserDB(User, models.BaseUserDB):
    pass

class ProductDB(BaseModel): 
    description: str
    price: float
    is_active: bool = True
