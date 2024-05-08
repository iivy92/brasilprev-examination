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
