from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

QUANTITY_OF_PROPERTIES = os.getenv("QUANTITY_OF_PROPERTIES")
NUMBER_SIMULATIONS = os.getenv("NUMBER_SIMULATIONS")
TIMEOUT_ROUND = os.getenv("TIMEOUT_ROUND")
PLAYER_INITIAL_MONEY = os.getenv("PLAYER_INITIAL_MONEY")
PLAYER_MONEY_ROUND = os.getenv("PLAYER_MONEY_ROUND")
