import pygame
from scenes.scene import Scene
from sprites.shark_sprite import Shark

class MainScene(Scene):
    def init(self):
        self.scene_number = 0

    def handle_event(self, event, delta_time):
        super().handle_event(event, delta_time)
        if (event.type == pygame.KEYDOWN):
            self.scene_number = 1

