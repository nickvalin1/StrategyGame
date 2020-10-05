from model.gamemap import Direction


class Unit:

    def __init__(self, name, weapon, stats):
        self.name = name
        self.weapon = weapon
        self.move = stats["move"]
        self.stats = {}
        self.abilities = []
        self.map_space = None

    def reposition(self, x, y, grid):
        map_space = grid[y][x]
        map_space.friendly_occupied = True
        self.map_space = map_space

    def attack(self, enemy):
        power = self.stats["strength"] + self.weapon.strength
        damage = power - enemy.stats["defense"]
        damage = damage if damage > 0 else 0
        enemy.stats["hp"] = enemy.stats["hp"] - (power - damage)

    def get_movement_options(self, game_map):
        return self.get_spaces(self.map_space.x, self.map_space.y, remaining=self.move, game_map=game_map)

    def get_spaces(self, x, y, remaining, game_map):
        spaces = []
        for d in Direction:
            space = game_map.move(x, y, d)
            if space and space.move_penalty * remaining >= 1 and not space.enemy_occupied:
                if not space.friendly_occupied or space == self.map_space:
                    spaces.append(space)
                new_remaining = (space.move_penalty * remaining) - 1
                spaces.extend(self.get_spaces(space.x, space.y, new_remaining, game_map))
        return list(set(spaces))
