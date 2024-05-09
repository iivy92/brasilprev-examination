from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

QUANTITY_OF_PROPERTIES = os.getenv("QUANTITY_OF_PROPERTIES", 20)
NUMBER_SIMULATIONS = os.getenv("NUMBER_SIMULATIONS", 300)
TIMEOUT_ROUND = os.getenv("TIMEOUT_ROUND", 1000)
PLAYER_INITIAL_MONEY = os.getenv("PLAYER_INITIAL_MONEY", 300.0)
PLAYER_MONEY_ROUND = os.getenv("PLAYER_MONEY_ROUND", 100.0)
