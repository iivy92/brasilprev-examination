import random
from datetime import datetime
from typing import List, Optional
from typing import List
from src.models.player import Player, PlayerStrategy
from src.models.property import Property
from src.models.board import Board
from src import config

class HandlerBoard:
    def __init__(self, players: List[Player], properties: List[Property]):
        self.players = players
        self.properties = properties
        self.board = Board(players=self.players, cards=self.properties)
    
    def walk(self, player: Player):
        print(f"\n- {player.strategy} is taking their turn with {player.money} money.")
        steps = self.roll_dice()
        print(f"- {player.strategy} rolled a {steps}.")

        player.position = (player.position + steps) % len(self.properties)
    
        if player.position < steps:
            print(f"- {player.strategy} completed a lap! They gained {config.PLAYER_MONEY_ROUND} in balance.")
            player.money += float(config.PLAYER_MONEY_ROUND)

        print(f"- {player.strategy} is now at position {player.position}.")
    
    def verify_property(self, player: Player):
        current_property = self.properties[player.position]
        if current_property.owner is None:
            self.buy_property(player, current_property)
        else:
            self.pay_rent(player, current_property)

    def buy_property(self, player: Player, property: Property):
        if self.decide_to_buy_property(player, property):
            player.money -= property.price
            property.owner = player
            print(f"- {player.strategy} buyed property {property.id} for {property.price} money.")
        else:
            print(f"- {player.strategy} doesn't wanna buy property {property.id}.")

    def pay_rent(self, player: Player, property: Property):
        if player != property.owner:
            print(f"- {player.strategy} is paying rent of {property.rent_price} to Player {property.owner.strategy}.")
            player.money -= property.rent_price
            property.owner.money += property.rent_price
        else:
            print(f"- {player.strategy} owns the property {property.id}.")

    def check_player_conditions(self, player: Player):
        if player.money < 0:
            print(f"- {player.strategy} has gone bankrupt and is out of the game.")
            player.gameover = True
            
            for property in self.properties:
                if property.owner == player:
                    property.owner = None
            
            return
        
        print(f"- {player.strategy} has {player.money} at the end of this turn.")
    
    def check_gameover(self) -> bool:
        active_players = [player for player in self.players if player.money > 0]
        if len(active_players) == 1:
            self.board.winner = active_players[0]
            print(f"\n- {self.board.winner.strategy} has won the game with {self.board.winner.money} money!")
            self.board.gameover = True
        elif len(active_players) == 0:
            print("\nNo active players left. It's a tie!")
            self.board.gameover = True
        elif self.board.plays >= int(config.TIMEOUT_ROUND):
            richest_player = max(self.players, key=lambda x: x.money)
            self.board.winner = richest_player
            self.board.gameover = True
            self.board.timed_out = True
    
    def roll_dice(self) -> int:
        return random.randint(1, 6)

    def decide_to_buy_property(self, player: Player, property: Property):
        if player.money < property.price:
            print(f"- {player.strategy} does not have enough money to buy property {property.id}.")
            return False
        
        if player.strategy == PlayerStrategy.IMPULSIVE:
            return True
        elif player.strategy == PlayerStrategy.DEMANDING:
            return property.rent_price > 50
        elif player.strategy == PlayerStrategy.CAUTIOUS:
            return player.money >= property.price + 80
        elif player.strategy == PlayerStrategy.RANDOM:
            return random.choice([True, False])
        
        return False

    def play_round(self):
        print(f"\n============ Turn {self.board.plays} ============")
        for player in self.players:
            if not player.gameover:
                self.walk(player)
                self.verify_property(player)
                self.check_player_conditions(player)
            
            self.check_gameover()
         
        if self.board.timed_out:
            print(f"\nGame ended after 1000 turns. Player {self.board.winner.strategy} with {self.board.winner.money} money wins!")
