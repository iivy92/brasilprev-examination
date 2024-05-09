import pytest
from src.services.board import HandlerBoard
from src.models.player import Player, PlayerStrategy
from src.models.property import Property

@pytest.fixture
def players():
    return [
        Player(id=1, money=300, position=0, strategy=PlayerStrategy.IMPULSIVE),
        Player(id=2, money=300, position=0, strategy=PlayerStrategy.DEMANDING),
        Player(id=3, money=300, position=0, strategy=PlayerStrategy.CAUTIOUS),
        Player(id=4, money=300, position=0, strategy=PlayerStrategy.RANDOM),
    ]

@pytest.fixture
def properties():
    return [
        Property(id=1, price=50, rent_price=10),
        Property(id=2, price=100, rent_price=20),
        Property(id=3, price=150, rent_price=30),
    ]

@pytest.fixture
def handler_board(players, properties):
    return HandlerBoard(players=players, properties=properties)

def test_board_initialization(handler_board):
    assert handler_board.board.winner is None
    assert handler_board.board.plays == 0
    assert len(handler_board.board.players) == 4
    assert len(handler_board.board.cards) == 3

# def test_player_movement(handler_board):
#     player = handler_board.players[0]
#     initial_position = player.position
#     handler_board.walk(player)
#     assert player.position != initial_position

def test_buy_property(handler_board):
    player = handler_board.players[0]
    player.position = 0
    initial_money = player.money
    handler_board.verify_property(player)
    assert player.money == initial_money - handler_board.properties[0].price
    assert handler_board.properties[0].owner == player

def test_pay_rent(handler_board):
    player1 = handler_board.players[0]
    player2 = handler_board.players[1]
    player1.position = 1
    player1.money = 300
    player2.money = 300
    handler_board.properties[1].owner = player2
    initial_money_player1 = player1.money
    initial_money_player2 = player2.money
    handler_board.verify_property(player1)
    assert player1.money == initial_money_player1 - handler_board.properties[1].rent_price
    assert player2.money == initial_money_player2 + handler_board.properties[1].rent_price

def test_game_over(handler_board):
    player = handler_board.players[0]
    player.gameover = False
    player.money = -2
    handler_board.check_player_conditions(player)
    assert player.gameover

