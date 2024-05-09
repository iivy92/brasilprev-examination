from src.models.player import Player, PlayerStrategy
import pytest

@pytest.fixture
def sample_player():
    return Player(money=300, position=0, strategy=PlayerStrategy.IMPULSIVE)

def test_create_player(sample_player):
    assert sample_player.money == 300
    assert sample_player.position == 0
    assert sample_player.strategy == PlayerStrategy.IMPULSIVE
    assert not sample_player.gameover

def test_create_player_with_custom_money_and_position():
    player = Player(money=500, position=2, strategy=PlayerStrategy.DEMANDING)
    assert player.money == 500
    assert player.position == 2
    assert player.strategy == PlayerStrategy.DEMANDING
    assert not player.gameover

def test_player_gameover():
    player = Player(money=50, position=0, strategy=PlayerStrategy.CAUTIOUS)
    player.gameover = True
    assert player.gameover

def test_player_update_money():
    player = Player(money=300, position=0, strategy=PlayerStrategy.RANDOM)
    player.money += 100
    assert player.money == 400

def test_player_update_position():
    player = Player(money=300, position=0, strategy=PlayerStrategy.IMPULSIVE)
    player.position = 5
    assert player.position == 5
