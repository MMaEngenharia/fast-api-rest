# Source: https://frankie567.github.io/fastapi-users/
#import uvicorn

from fastapi import FastAPI
from src.model import *
from src.security import fastapi_users, on_after_register, on_after_forgot_password
from src.authentication import jwt_authentication, SECRET
from src.database import *

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)

app.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])

@app.get("/products")
def read_products():
    return database_name.products.find()

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)