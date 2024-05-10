import pytest

from src.models.player import Player, PlayerStrategy


@pytest.fixture
def sample_player():
    return Player(id=1, money=300, position=0, strategy=PlayerStrategy.IMPULSIVE)


def test_create_player(sample_player):
    assert sample_player.id == 1
    assert sample_player.money == 300
    assert sample_player.position == 0
    assert sample_player.strategy == PlayerStrategy.IMPULSIVE
    assert not sample_player.gameover


def test_create_player_with_custom_money_and_position():
    player = Player(id=2, money=500, position=2, strategy=PlayerStrategy.DEMANDING)
    assert player.id == 2
    assert player.money == 500
    assert player.position == 2
    assert player.strategy == PlayerStrategy.DEMANDING
    assert not player.gameover


def test_player_gameover():
    player = Player(id=3, money=50, position=0, strategy=PlayerStrategy.CAUTIOUS)
    player.gameover = True
    assert player.gameover


def test_player_update_money():
    player = Player(id=4, money=300, position=0, strategy=PlayerStrategy.RANDOM)
    player.money += 100
    assert player.money == 400


def test_player_update_position(sample_player):
    sample_player.position += 5
    assert sample_player.position == 5
