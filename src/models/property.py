import random
from pydantic import BaseModel
from src.models.player import Players

class Property(BaseModel):
    id: int
    owner: Players = None
    price: int = random.randint(20, 110)
    rent_price: int = price/2