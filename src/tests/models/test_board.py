from datetime import datetime
import pytest
from src.models.board import Board
from src.models.player import Player, PlayerStrategy
from src.models.property import Property
from src import config

@pytest.fixture
def players():
    return [
        Player(id=1, money=config.PLAYER_INITIAL_MONEY, strategy=PlayerStrategy.IMPULSIVE),
        Player(id=2, money=config.PLAYER_INITIAL_MONEY, strategy=PlayerStrategy.DEMANDING),
        Player(id=3, money=config.PLAYER_INITIAL_MONEY, strategy=PlayerStrategy.CAUTIOUS),
        Player(id=4, money=config.PLAYER_INITIAL_MONEY, strategy=PlayerStrategy.RANDOM),
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
    assert len(board.players) == 4
    assert len(board.cards) == 7

def test_board_update_winner(board, players):
    winner_player = players[0]
    board.winner = winner_player
    assert board.winner == winner_player

def test_board_update_plays(board):
    board.plays += 10
    assert board.plays == 10

def test_board_gameover(board, players):
    winner_player = players[0]
    board.winner = winner_player
    board.gameover = True
    assert board.gameover == True

def test_board_timed_out(board):
    board.plays = 1001
    board.timed_out = True
    assert board.timed_out == True
