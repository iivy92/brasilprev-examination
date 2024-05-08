from datetime import datetime
import pytest
from src.models.board import Board
from src.models.player import Player, PlayerStrategy
from src.models.property import Property

@pytest.fixture
def players():
    return [
        Player(money=500, strategy=PlayerStrategy.IMPULSIVE),
        Player(money=400, strategy=PlayerStrategy.DEMANDING),
        Player(money=600, strategy=PlayerStrategy.CAUTIOUS),
        Player(money=600, strategy=PlayerStrategy.RANDOM),
    ]

@pytest.fixture
def properties(players):
    return [
        Property(id=1),
        Property(id=2),
        Property(id=3),
        Property(id=4),
        Property(id=5),
        Property(id=6),
        Property(id=7),
    ]

@pytest.fixture
def board(players, properties):
    return Board(winner=None, plays=0, start_time=datetime.now(), players=players, cards=properties)

def test_board_initialization(board):
    assert board.winner is None
    assert board.plays == 0
    assert isinstance(board.start_time, datetime)
    assert len(board.players) == 4
    assert len(board.cards) == 7
