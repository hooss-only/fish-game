import pygame
from scenes.scene import Scene
from sprites.test_sprite import TestSprite

class TestScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.sprites.append(TestSprite(self.screen))
