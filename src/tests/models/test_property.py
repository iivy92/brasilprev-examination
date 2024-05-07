import random
import pytest
from src.models.player import Player, PlayerStrategy
from src.models.property import Property

@pytest.fixture
def sample_property():
    return Property(id=1)

def test_create_property(sample_property):
    assert sample_property.id == 1
    assert sample_property.owner is None
    assert 20 <= sample_property.cost <= 110
    assert 20 <= sample_property.rent <= 110

def test_create_property_with_custom_values():
    player = Player(money=500, strategy=PlayerStrategy.DEMANDING)
    prop = Property(id=2, cost=100, rent=80, owner=player)
    assert prop.id == 2
    assert prop.cost == 100
    assert prop.rent == 80
    assert prop.owner == player

def test_invalid_property_creation():
    with pytest.raises(ValueError):
        Property(id=3, cost=10, rent=200, owner="Player2")

def test_update_property_owner():
    player1 = Player(money=500, strategy=PlayerStrategy.DEMANDING)
    prop = Property(id=4)
    prop.owner = player1
    assert prop.owner == player1
    prop.owner = None
    assert prop.owner == None
