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

@pytest.fixture
def games(players, properties):
    return [
        Board(plays=10, cards=properties, players=players, winner=players[0]),
        Board(plays=15, cards=properties, players=players, winner=players[1]),
        Board(plays=20, cards=properties, players=players, winner=players[2]),
        Board(plays=10, cards=properties, players=players, winner=players[3]),
        Board(plays=15, cards=properties, players=players, winner=players[0]),
        Board(plays=20, cards=properties, players=players, winner=players[1]),
        Board(plays=25, cards=properties, players=players, winner=players[1])
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

def test_calculate_average_turns(metrics_handler, games):
    for game in games:
        metrics_handler.save_metrics(game)
    
    expected_average = (10 + 15 + 20 + 10 + 15 + 20 + 25) / 7
    
    assert metrics_handler.calculate_average_turns() == expected_average

def test_calculate_percentage_wins_by_strategy(metrics_handler, games):
    for game in games:
        metrics_handler.save_metrics(game)
    
    expected_percentages = {
        PlayerStrategy.IMPULSIVE: 2 / len(games) * 100,
        PlayerStrategy.DEMANDING: 3 / len(games) * 100,
        PlayerStrategy.CAUTIOUS: 1 / len(games) * 100,
        PlayerStrategy.RANDOM: 1 / len(games) * 100
    }
    
    assert metrics_handler.calculate_percentage_wins_by_strategy() == expected_percentages

def test_calculate_wins_by_strategy(metrics_handler, games):
    for game in games:
        metrics_handler.save_metrics(game)

    expected_wins = {
        PlayerStrategy.IMPULSIVE: 2,
        PlayerStrategy.DEMANDING: 3,
        PlayerStrategy.CAUTIOUS: 1,
        PlayerStrategy.RANDOM: 1
    }

    assert metrics_handler.calculate_wins_by_strategy() == expected_wins
