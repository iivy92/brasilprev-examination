import pytest
from src.models.board import Board
from src.services.metrics import HandlerMetrics
from src.models.player import Player, PlayerStrategy
from src.models.property import Property

@pytest.fixture
def metrics_handler():
    return HandlerMetrics()

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

def test_save_metrics(metrics_handler, players, properties):
    game_board = Board(winner=players[1], plays=10, timed_out=False, cards=properties, players=players)
    
    metrics_handler.save_metrics(game_board)
    
    assert len(metrics_handler.rounds) == 1
    assert metrics_handler.rounds[0]["timed_out"] == False
    assert metrics_handler.rounds[0]["turns"] == 10
    assert metrics_handler.rounds[0]["winner"] == PlayerStrategy.DEMANDING

def test_calculate_timed_out_games(metrics_handler):
    metrics_handler.rounds = [
        {"timed_out": True},
        {"timed_out": False},
        {"timed_out": True},
        {"timed_out": False}
    ]

    timed_out_games = metrics_handler.calculate_timed_out_games()

    assert timed_out_games == 2
