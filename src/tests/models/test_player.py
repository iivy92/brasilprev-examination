from src.models.player import Player
import pytest

@pytest.fixture
def sample_player():
    return Player(strategy="Impulsive")

def test_create_player(sample_player):
    assert sample_player.money == 300
    assert sample_player.position == 0
    assert sample_player.strategy == "Impulsive"
    assert not sample_player.gameover

def test_create_player_with_custom_money_and_position():
    player = Player(money=500, position=2, strategy="Exigent")
    assert player.money == 500
    assert player.position == 2
    assert player.strategy == "Exigent"
    assert not player.gameover

