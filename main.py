#import asyncio
#from fastapi import FastAPI
from src.services.game import GameSimulation

def main():
    game_simulation = GameSimulation()
    game_simulation.start_game()

if __name__ == "__main__":
    main()
