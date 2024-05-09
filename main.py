#import asyncio
#from fastapi import FastAPI
from src.services.simulation import HandlerSimulation

def main():
    game_simulation = HandlerSimulation()
    game_simulation.start_game()

if __name__ == "__main__":
    main()
