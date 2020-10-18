from controler.input_context import InputContext


class MapContext(InputContext):

    def down(self, event):
        if self.parent.level.game_map.move(0, 1):
            r = self.parent.level.tile_map.range
            if self.parent.level.game_map.y >= r[1][1]:
                self.parent.level.tile_map.range = (r[0], (r[1][0] + 1, r[1][1] + 1))
            self.parent.level.render()
            return True
        else:
            return False

    def up(self, event):
        if self.parent.level.game_map.move(0, -1):
            r = self.parent.level.tile_map.range
            if self.parent.level.game_map.y < r[1][0]:
                self.parent.level.tile_map.range = (r[0], (r[1][0] - 1, r[1][1] - 1))
            self.parent.level.render()
            return True
        else:
            return False

    def left(self, event):
        if self.parent.level.game_map.move(-1, 0):
            r = self.parent.level.tile_map.range
            if self.parent.level.game_map.x < r[0][0]:
                self.parent.level.tile_map.range = ((r[0][0] - 1, r[0][1] - 1), r[1])
            self.parent.level.render()
            return True
        else:
            return False

    def right(self, event):
        if self.parent.level.game_map.move(1, 0):
            r = self.parent.level.tile_map.range
            if self.parent.level.game_map.x >= r[0][1]:
                self.parent.level.tile_map.range = ((r[0][0] + 1, r[0][1] + 1), r[1])
            self.parent.level.render()
            return True
        else:
            return False
