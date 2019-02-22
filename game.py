from player import Player


class Game:
    def __init__(self, id, timestep):
        self.players = []
        for i in range(10):
            self.players.append(Player(timestep, i))
        self.id = id
