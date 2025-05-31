import pygame
from sprites.sprite import Sprite

class TestSprite(Sprite):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.image = pygame.image.load('./assets/pepe.png').convert()
        self.x = 100; self.y = 100
