from src.models.board import Board

class HandlerMetrics:
    def __init__(self):
        self.rounds = []
    
    def save_metrics(self, board_game: Board):
        metrics = {
            "timed_out": board_game.timed_out,
            "turns": board_game.plays,
            "winner": board_game.winner.strategy,
        }
        
        self.rounds.append(metrics)
    
