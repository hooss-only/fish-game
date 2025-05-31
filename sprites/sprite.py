import pygame

class Sprite:
    x=0; y=0
    screen: pygame.Surface
    image: pygame.Surface

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))
    
    def tick(self):
        return

