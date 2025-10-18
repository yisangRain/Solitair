import numpy as np


class IDisplay:
    BOARD: np.ndarray = np.array([])

    def __init__(self):
        self.startState: np.ndarray = self.BOARD.copy()

    def restart_board(self):
        self.BOARD = self.startState.copy()
        print("Board reset to initial state.")

    def show_board(self):
        return self.BOARD

    def update_board(self, newState: np.ndarray):
        self.BOARD = newState
        print("Board updated.")

    def setup_board(self, config: dict):
        raise NotImplementedError(
            "setup_board method must be implemented by subclasses"
        )
