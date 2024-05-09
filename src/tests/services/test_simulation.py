import pytest

from src import config
from src.models.player import Player, PlayerStrategy
from src.models.property import Property
from src.services.simulation import HandlerSimulation


@pytest.fixture
def simulation():
    return HandlerSimulation()

def test_create_players(simulation):
    players = simulation.create_players()
    assert len(players) == 4
    assert all(isinstance(player, Player) for player in players)
    assert all(player.strategy in list(PlayerStrategy) for player in players)

def test_create_cards(simulation):
    cards = simulation.create_cards()
    assert len(cards) == int(config.QUANTITY_OF_PROPERTIES)
    assert all(isinstance(card, Property) for card in cards)
    assert all(card.id is not None for card in cards)
    assert all(card.price is not None for card in cards)
    assert all(card.rent_price is not None for card in cards)
