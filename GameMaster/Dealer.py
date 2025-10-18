import click
import Games.IGameMode as gameMode
import Games.IDisplay as gameDisplay
import Games.IRule as gameRule


class Dealer:
    def __init__(self):
        self.gameMode: gameMode = None
        self.gameDisplay: gameDisplay = None
        self.gameRule: gameRule = None
        self.numberOfTurns = 0

    def select_game_mode(self):
        # Placeholder for selecting game mode logic
        gameType: int = int(
            click.prompt(
                "Please select a game mode: \n \
              [1] Classic Solitaire"
            ).strip()
        )

        print(gameType)

    def initialize(self):
        print("Dealer is setting up the game...")
        # Initialize game state, shuffle deck, deal cards, etc.
        # Placeholder for actual game initialization logic
        print("Game initialized. Ready to play!")
