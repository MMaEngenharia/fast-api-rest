import motor.motor_asyncio
from fastapi_users.db import MongoDBUserDatabase
from src.model import UserDB, ProductDB

# Create Database in https://www.mongodb.com/
DATABASE_URL = "mongodb+srv://admin:SENHA@cluster0.zripw.mongodb.net/admin?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)

# Name of DataBase
database_name = client["fast_api_db"]

# Collections
users = database_name["users"]
products = database_name["products"]

user_db = MongoDBUserDatabase(UserDB, users)