import random
from typing import List
from src import config
from src.services.board import HandlerBoard
from src.services.metrics import HandlerMetrics
from src.models.player import Player, PlayerStrategy
from src.models.property import Property

class HandlerSimulation:
    def __init__(self):
        self.board_handler = None
        self.metrics_handler = HandlerMetrics()
    
    def start_game(self):
        print("================Starting the game simulation!================")

        self.board_handler = HandlerBoard(self.create_players(), self.create_cards())

        while not self.board_handler.board.gameover:
            self.board_handler.board.plays += 1
            self.board_handler.play_round()
        
        self.metrics_handler.save_metrics(self.board_handler.board)
        print(self.metrics_handler.rounds)
        print("================Ending the game simulation!================")
    
    def create_players(self) -> List[Player]:
        strategies = list(PlayerStrategy)
        random.shuffle(strategies)
        players = [Player(id=strategy.value, strategy=strategy) for strategy in strategies]

        return players
    
    def create_cards(self) -> List[Property]:
        cards = []
        quantity_of_properties = int(config.QUANTITY_OF_PROPERTIES)
        for i in range(0, quantity_of_properties):
            price = random.randint(20, 150)
            rent_price = price/2
            cards.append(Property(id=i, price=price, rent_price=rent_price))

        return cards