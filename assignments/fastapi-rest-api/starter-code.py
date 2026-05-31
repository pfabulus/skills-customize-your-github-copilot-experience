from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

items: List[Item] = [
    Item(id=1, name="Sample Item", description="Example product", price=9.99)
]

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items.pop(index)
            return
    raise HTTPException(status_code=404, detail="Item not found")
