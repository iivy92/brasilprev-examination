from pydantic import BaseModel

class Player(BaseModel):
    money: int = 300
    position: int = 0
    strategy: str
    gameover: bool = False
