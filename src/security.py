from fastapi import Request
from fastapi_users import FastAPIUsers
from src.model import *
from src.database import user_db
from src.authentication import jwt_authentication

def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")

def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")

fastapi_users = FastAPIUsers(
    user_db, [jwt_authentication], User, UserCreate, UserUpdate, UserDB,
)