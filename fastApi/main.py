from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from enum import Enum
from enums import ModelName

app = FastAPI()


@app.get("/mods/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/test")
async def read_test():
    async def read_item(skip: int = 0, limit: int = 100):
        return [{"id": 1, "title": "The Shawshank Redemption", "year": 1994}]
    return await read_item()

@app.get('/usr')
async def read_user(firstname: str, lastname: str):
    return {"fullname": get_full_name(firstname, lastname)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

def get_full_name(firstname: str, lastname: str):
    fullname = firstname.title() + " " + lastname.title()
    return fullname

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost" , port=8000)

    print(get_full_name("john", "doe"))