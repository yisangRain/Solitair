import IGameMode


class SolitairRules(IGameMode):
    gameMode: str = "Classic Solitaire"
    playerCount: int = 1

    def __init__(self):
        pass

    def start_game(self):
        print("Starting Classic Solitaire with 1 player.")
