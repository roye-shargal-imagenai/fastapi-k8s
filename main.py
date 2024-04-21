from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

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
@app.get("/get_data_from_mongodb")
async def get_data_from_mongodb():
    # Example query to retrieve data from MongoDB
    all_users = users_collections.find({})
    return all_users