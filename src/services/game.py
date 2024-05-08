from datetime import datetime
from typing import List, Optional
import random
from .player import Player
from .property import Property
from .board import Board
from src import config

class Game:
    def __init__(self,):
        self.players = create_players()
        self.properties = create_cards()
        self.board = Board(players=players, cards=properties)

    def create_players() -> List[Player]:
        strategies = list(PlayerStrategy)
        random.shuffle(strategies)
        players = [Player(id=strategy.value, strategy=strategy) for strategy in strategies]

        return players
    
    def create_cards() -> List[Property]:
        quantity_of_properties = config.QUANTITY_OF_PROPERTIES
        cards = [Property(id=i) for i in range(1, quantity_of_properties)]

        return cards
    
    def walk(self, player: Player):
        print(f"\nPlayer {player.strategy} is taking their turn.")
        steps = self.roll_dice()
        print(f"Player {player.strategy} rolled a {steps}.")

        player.position = (player.position + steps) % len(self.properties)
        print(f"Player {player.strategy} is now at position {player.position}.")
    
    def verify_position(self, player: Player):
        if player.position < steps:
            print(f"Player {player.strategy} completed a lap! They gained 100 in balance.")
            player.money += config.PLAYER_MONEY_ROUND

    def verify_property(self, player: Player):
        current_property = self.properties[player.position]
        if current_property.owner is None:
            self.buy_property(player, current_property)
        else:
            self.pay_rent(player, current_property)

    def buy_property(self, player: Player, property: Property):
        if decide_to_buy_property(player, Property):
            player.money -= property.price
            property.owner = player
            print(f"Player {player.strategy} now owns property {property.id}.")
        else:
            print(f"Player {player.strategy} doesn't wanna buy property {property.id}.")

    def pay_rent(self, player: Player, property: Property):
        if player != property.owner:
            print(f"Player {player.strategy} is paying rent of {property.rent_price} to Player {property.owner.strategy}.")
            player.money -= property.rent_price
            property.owner.money += property.rent_price

    def check_player_conditions(self, player: Player):
        if player.money < 0:
            print(f"Player {player.strategy} has gone bankrupt and is out of the game.")
            player.gameover = True
            
            for property in self.properties:
                if property.owner == player:
                    property.owner = None
    
    def check_gameover(self) -> bool:
        active_players = [player for player in self.players if player.money > 0]
        if len(active_players) == 1:
            self.board.winner = active_players[0]
            print(f"\nPlayer {self.board.winner.strategy} has won the game with {self.board.winner.money} money!")
            self.board.gameover = True
        elif len(active_players) == 0:
            print("\nNo active players left. It's a tie!")
            self.board.gameover = True
        elif self.board.plays >= 1000:
            richest_player = max(self.players, key=lambda x: x.money)
            self.board.winner = richest_player
            print(f"\nGame ended after 1000 turns. Player {richest_player.strategy} with {richest_player.money} money wins!")
            self.board.gameover = True
    
    def roll_dice(self) -> int:
        return random.randint(1, 6)

    def decide_to_buy_property(self, player: Player, property: Property):
        if player.money < property.price:
            print(f"Player {player.strategy} does not have enough money to buy property {property.id}.")
            return False
        
        if player.strategy == PlayerStrategy.IMPULSIVE:
            return True
        elif player.strategy == PlayerStrategy.DEMANDING:
            return property.rent > 50
        elif player.strategy == PlayerStrategy.CAUTIOUS:
            return player.money >= property.price + 80
        elif player.strategy == PlayerStrategy.RANDOM:
            return random.choice([True, False])
        
        return False

    def start_game(self):
        print("Starting the game!")
        self.board.start_time = datetime.now()

        while not self.board.gameover:
            self.board.plays += 1
            self.play_round()

    def play_round(self):
        print(f"\n=== Turn {self.board.plays} ===")
        for player in self.players:
            if not player.gameover:
                self.walk(player)
                self.verify_position(player)
                self.verify_property(player)
                self.check_player_conditions(player)
                self.check_gameover()

