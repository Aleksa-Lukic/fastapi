from typing import Type
from pydantic import BaseModel, Field
from fastapi import Body, FastAPI
from enum import Enum

items = [
    {"Vorname": "Aleksa", "Nachname": "Lukic", "Alter": 25, "Abteiliung": "Managment"}
]

# Enum Object for 
class Type(Enum):
    salesdepartment: str = "Salesdepartment"
    management: str = "Management"


# Create a DataModel for the benefits with typehinten as validation for the data.
class Userdata(BaseModel):
    firstname: str
    lastname: str
    age: int
    department: Type
    

class ResponseItem(BaseModel):
    firstname: str
    department: Type



app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return items[user_id]


@app.post("/users/", response_model=ResponseItem)
async def create_user(data: Userdata):
    return items.append(data)


@app.put("/users/{user_id}")
async def change_value(user_id: int, user_data: Userdata):
    items[user_id] = user_data
    return user_data    
