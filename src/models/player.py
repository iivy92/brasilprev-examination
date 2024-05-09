from pydantic import BaseModel
from enum import Enum
from src import config


class PlayerStrategy(Enum):
    IMPULSIVE = 1
    DEMANDING = 2
    CAUTIOUS = 3
    RANDOM = 4


class Player(BaseModel):
    id: int
    money: float = 300
    position: int = 0
    strategy: PlayerStrategy
    gameover: bool = False
