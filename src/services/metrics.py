from src.models.board import Board
from src.models.player import PlayerStrategy


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

    def calculate_statistics(self) -> dict:
        timed_out_games = self.calculate_timed_out_games()
        average_turns = self.calculate_average_turns()
        percentage_wins_by_strategy = self.calculate_percentage_wins_by_strategy()
        most_winning_strategy = self.find_most_winning_strategy()

        statistics = {
            "timed_out_games": timed_out_games,
            "average_turns": average_turns,
            "percentage_wins_by_strategy": percentage_wins_by_strategy,
            "most_winning_strategy": most_winning_strategy,
        }

        return statistics

    def calculate_timed_out_games(self) -> int:
        return sum(1 for metrics in self.rounds if metrics["timed_out"])

    def calculate_average_turns(self) -> float:
        total_games = len(self.rounds)
        total_turns = sum(metrics["turns"] for metrics in self.rounds)
        return total_turns / total_games if total_games else 0

    def calculate_percentage_wins_by_strategy(self) -> dict:
        total_games = len(self.rounds)
        wins_by_strategy = self.calculate_wins_by_strategy()
        return {
            strategy: (wins / total_games) * 100
            for strategy, wins in wins_by_strategy.items()
        }

    def calculate_wins_by_strategy(self) -> dict:
        wins_by_strategy = {}
        for metrics in self.rounds:
            winner_strategy = metrics["winner"]
            if winner_strategy not in wins_by_strategy:
                wins_by_strategy[winner_strategy] = 0
            wins_by_strategy[winner_strategy] += 1
        return wins_by_strategy

    def find_most_winning_strategy(self) -> PlayerStrategy:
        wins_by_strategy = self.calculate_wins_by_strategy()
        return max(wins_by_strategy, key=wins_by_strategy.get)

    def print_statistics(self, statistics: dict):
        print("\n\n========================= Game Statistics =========================")
        print(f"Total games: {len(self.rounds)}\n")
        print(f"Total timed-out games: {statistics['timed_out_games']}\n")
        print(f"Average turns per game: {statistics['average_turns']:.2f}\n")
        print("Percentage of wins by strategy:")
        for strategy, percentage in statistics["percentage_wins_by_strategy"].items():
            print(f"  - {strategy.name}: {percentage:.2f}%")
        print(f"\nMost winning strategy: {statistics['most_winning_strategy'].name}\n")
