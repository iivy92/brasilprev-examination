import random
from pydantic import BaseModel
from src.models.player import Player

class Property(BaseModel):
    id: int
    owner: Player = None
    price: int = random.randint(20, 110)
    rent_price: int = price/2