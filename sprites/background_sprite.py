import pygame
from sprites.sprite import Sprite

class BackgroundSprite(Sprite):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.image = pygame.image.load('./assets/background.jpg').convert()
        self.image = pygame.transform.scale(self.image, 
                (self.image.get_width() * 0.7,
                self.image.get_height() * 0.7)
        )

