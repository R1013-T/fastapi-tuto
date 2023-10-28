from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: bool = None

@app.get("/hello")
async def hello():
  return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
  return {"item_id ====>": item_id, "q ====>": q}

@app.put("/items/{item_id}")
def update_item(item_od: int, item: Item):
  return {"item_name": item.name, "item_id": item.id}