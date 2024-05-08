from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from .player import Player
from .property import Property

class Board(BaseModel):
    start_time: datetime = datetime.now()
    winner: Optional[Player] = None
    plays: int = 0
    players: List[Player]
    cards: List[Property]
