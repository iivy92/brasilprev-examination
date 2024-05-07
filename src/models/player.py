from pydantic import BaseModel
from enum import Enum

class PlayerStrategy(str, Enum):
    IMPULSIVE = "Impulsive"
    DEMANDING = "Demanding"
    CAUTIOUS = "Cautious"
    RANDOM = "Random"

class Player(BaseModel):
    money: int = 300
    position: int = 0
    strategy: str
    gameover: bool = False
