class IRule:
    def __init__(self):
        pass

    def validate_move(self, move: dict) -> bool:
        raise NotImplementedError(
            "validate_move method must be implemented by subclasses"
        )

    def check_win_condition(self, game_state: dict) -> bool:
        raise NotImplementedError(
            "check_win_condition method must be implemented by subclasses"
        )
