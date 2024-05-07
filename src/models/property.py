import random
from pydantic import BaseModel
from src.models.player import Player

class Property(BaseModel):
    id: int
    owner: Player = None
    cost: int = random.randint(20, 110)
    rent: int = random.randint(20, 110)