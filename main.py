from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import date

app = FastAPI()

SECRET_KEY = "secret-key"
ALGORITHM = "HS256"
users = [{"id": 1, "name": "roye"}]


@app.get("/health")
async def root():
    return {"message": "Hello World"}


class User(BaseModel):
    name: str
    lastname: str


@app.post("/new-user")
async def sign_up(user: User):
    users.append(user)
    return "Added user successfully :), userid: %s" % user.name


@app.get("/users")
async def get_users():
    return users


@app.get("/users/{user_id}")
def get_single_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return "None"
