from enum import Enum

from pydantic import BaseModel

from src import config


class PlayerStrategy(Enum):
    IMPULSIVE = 1
    DEMANDING = 2
    CAUTIOUS = 3
    RANDOM = 4


class Player(BaseModel):
    id: int
    money: float = float(config.PLAYER_INITIAL_MONEY)
    position: int = 0
    strategy: PlayerStrategy
    gameover: bool = False
