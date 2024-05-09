#import asyncio
#from fastapi import FastAPI
from src.services.board import HandlerBoard

def main():
    game_simulation = HandlerBoard()
    game_simulation.start_game()

if __name__ == "__main__":
    main()
