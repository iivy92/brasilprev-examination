import random
from pydantic import BaseModel
from src.models.player import Player

class Property(BaseModel):
    id: int
    owner: Player = None
    price: float = None
    rent_price: float = None