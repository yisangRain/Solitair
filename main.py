import click
import sys
from Common import StandardResponses
from GameMaster import Dealer


def main():
    print("Welcome to CLI Solitaire")
    print("This is a simple command-line interface for various standard card games.")

    command = (
        click.prompt(
            "Would you like to start a game or quit?\n \
        Type `yes` to start\n \
        Type 'no' to quit.",
            type=str,
        )
        .strip()
        .lower()
    )

    if command in StandardResponses.affirmation:
        print("Bringing in the Dealer...")
        dealer = Dealer.Dealer()

        dealer.select_game_mode()

        dealer.initialize()

    print("Thank you for playing CLI Solitaire. Goodbye!")
    sys.exit(0)


if __name__ == "__main__":
    main()
