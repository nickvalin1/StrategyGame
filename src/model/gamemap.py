import json
from enum import Enum


class GameMap:

    def __init__(self, map_path):
        with open(map_path) as map_file:
            map_doc = json.load(map_file)
        self.grid = self.build_grid(map_doc)
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        properties = {property["name"]: property["value"] for property in map_doc["properties"]}
        self.units = properties["units"]
        self.starting_positions = [tuple(map(int, position.split(",")))
                                   for position in properties["starting_positions"].split(";")]
        self.victory_condition = None
        self.defeat_conditions = []
        self.turn_count = 0
        self.x, self.y = self.starting_positions[0]

    def build_grid(self, map_doc):
        tiles = map_doc["tilesets"][0]["tiles"]
        grid = []
        properties = {tile["id"]: tile["properties"] for tile in tiles}
        for i, code in enumerate(map_doc["layers"][0]["data"]):
            x = i // map_doc["width"]
            y = i % map_doc["width"]
            properties = properties.get(code, {})
            if y == 0:
                grid.append([MapSpace(x, y, **properties)])
            else:
                grid[x].append(MapSpace(x, y, **properties))
        return grid

    def move(self, x, y):
        new_x = self.x + x
        new_y = self.y + y
        if new_x >= self.width or new_y >= self.height or new_x < 0 or new_y < 0:
            return
        self.x = new_x
        self.y = new_y
        space = self.grid[new_y][new_x]
        return space


class MapSpace:

    def __init__(self, x, y, move_penalty=1, defense=0, avoid=0):
        self.x, self.y = (x, y)
        self.move_penalty = move_penalty
        self.defense = defense
        self.avoid = avoid
        self.friendly_occupied = False
        self.enemy_occupied = False


class VictoryCondition(Enum):

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def defend(self):
        return bool(self.kwargs["turn"] > self.kwargs["n"])

    def seize(self):
        # Add menu option for seize
        pass


# class Direction(Enum):
#     UP = (0, -1)
#     LEFT = (-1, 0)
#     DOWN = (0, 1)
#     RIGHT = (1, 0)
