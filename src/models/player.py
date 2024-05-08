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
    money: int = config.PLAYER_INITIAL_MONEY
    position: int = 0
    strategy: PlayerStrategy
    gameover: bool = False


    def verify_property(self, property, board=None):
        if property.owner:
            if self != property.owner:
                self.pay_rent(property)
            return

        if self._decide_to_buy_property():
            property.owner = self

    def pay_rent(self, property):
        self.money -= property.rent_price
    
    def _decide_to_buy_property(self, property):
        if self.strategy == PlayerStrategy.IMPULSIVE:
            return True
        elif self.strategy == PlayerStrategy.DEMANDING:
            return property.rent > 50
        elif self.strategy == PlayerStrategy.CAUTIOUS:
            return self.money >= property.price + 80
        elif self.strategy == PlayerStrategy.RANDOM:
            return random.choice([True, False])
        
        return False
