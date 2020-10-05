from model.errors import GameOverError


class Party:

    def __init__(self, units, leader):
        self.units = units
        self.leader = leader

    def recruit(self, unit):
        self.units.append(unit)

    def death(self, unit):
        if self.leader == unit:
            raise GameOverError(f"{self.leader.name}, the party leader, has been defeated")
        self.units.remove(unit)
