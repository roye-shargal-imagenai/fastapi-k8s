from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pymongo import MongoClient
from bson import json_util  # Import json_util from bson module

app = FastAPI()

client = MongoClient("mongodb://roye:pass@localhost:27017/")
db = client.local
users_collections = db.users

class User(BaseModel):
    name: str
    email: str
    password: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/sign_up")
async def sign_up(user: User):
    # Example code to insert data into MongoDB
    users_collections.insert_one({
        "name": user.name,
        "email": user.email,
        "password": user.password
    })
    return {"message": "User created successfully"}



# Example route to query MongoDB
@app.get("/users")
async def get_all_users():
    # Example query to retrieve data from MongoDB
    all_users = list(users_collections.find({}, {"_id": 0}))
    # Serialize BSON objects to JSON
    print(all_users)
    # serialized_users = json_util.dumps(all_users)
    # Return JSONResponse
    return JSONResponse(content=all_users, status_code=200)