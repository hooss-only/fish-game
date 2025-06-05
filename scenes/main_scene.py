import pygame
from scenes.scene import Scene

class MainScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.scene_number = 0
    
    def handle_event(self, event, delta_time):
        super().handle_event(event, delta_time)
        if (event.type == pygame.KEYDOWN):
            self.scene_number = 1
