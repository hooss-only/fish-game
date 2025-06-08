import pygame
from sprites.sprite import Sprite

class DangerSprite(Sprite):
    def __init__(self, screen: pygame.Surface, rect: pygame.Rect, scene):
        super().__init__(screen)
        self.scene = scene
        self.rect = rect
        self.alpha = 128
        self.down = True
        self.speed = 5
        self.timer = 0

    def tick(self, delta_time):
        self.timer += 1
        if self.down:
            if self.alpha > 0:
                self.alpha -= self.speed
            else:
                self.down = False
        else:
            if self.alpha < 128:
                self.alpha += self.speed
            else:
                self.down = True

        if self.timer > 100:
            self.scene.showtime()
            self.delete_self()

    def render(self):
        s = pygame.Surface((self.rect.width, self.rect.height))
        s.set_alpha(self.alpha)
        s.fill((255, 0, 0))
        self.screen.blit(s, (self.rect.x, self.rect.y))
