from controler.input_context import InputContext


class MapContext(InputContext):

    def down(self, event):
        if self.parent.level.game_map.move(0, 1):
            self.parent.level.render()
            return True
        else:
            return False

    def up(self, event):
        if self.parent.level.game_map.move(0, -1):
            self.parent.level.render()
            return True
        else:
            return False

    def left(self, event):
        if self.parent.level.game_map.move(-1, 0):
            self.parent.level.render()
            return True
        else:
            return False

    def right(self, event):
        if self.parent.level.game_map.move(1, 0):
            self.parent.level.render()
            return True
        else:
            return False
