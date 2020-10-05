from controler.contexts.map_context import MapContext
import pygame


class InputHandler:

    def __init__(self, level):
        self.level = level
        self.context = MapContext(self)

    def handle_event(self, event):
        self.context.handle_event(event)

    def switch_context(self, context):
        self.context = context
