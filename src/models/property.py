import random
from pydantic import BaseModel
from src.models.player import Player

class Property(BaseModel):
    id: int
    owner: Player = None
    price: float = random.randint(20, 110)
    rent_price: float = price/2