class IGameMode:
    GAMENAME: str
    PLAYERCOUNT: int
    JOKERSALLOWED: bool

    def __init__(self):
        pass

    def start_game(self):
        raise NotImplementedError("start_game method must be implemented by subclasses")

    def setup_game(self):
        raise NotImplementedError("setup_game method must be implemented by subclasses")

    def play_turn(self):
        raise NotImplementedError("play_turn method must be implemented by subclasses")

    def end_game(self):
        raise NotImplementedError("end_game method must be implemented by subclasses")
