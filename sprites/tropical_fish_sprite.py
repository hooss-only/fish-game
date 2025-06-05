import pygame
import random
from sprites.sprite import Sprite

class TropicalFish(Sprite):
    def __init__(self, screen: pygame.Surface, player):
        super().__init__(screen)
        self.image = pygame.image.load('./assets/tropical_fish.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,
            (self.image.get_width() * 0.4,
            self.image.get_height() * 0.4)
        )

        self.fit_rect_size_to_image()
        
        self.speed = random.randint(100, 1000)
        self.direction = random.choice([-1, 1])

        self.rect.y = random.randint(0, screen.get_height() - self.image.get_height())
        
        self.player = player

        if (self.direction == -1):
            self.rect.x = screen.get_width() + self.image.get_width()
        else:
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x = -self.image.get_width()

    def tick(self, delta_time):
        self.rect.x += self.direction * self.speed * delta_time

        if pygame.Rect.colliderect(self.get_hitbox(), self.player.get_hitbox()):
            self.player.get_point()
            self.delete_self()

        if (self.direction == -1 and self.rect.x < -self.image.get_width()) or (self.direction == 1 and self.rect.x > self.screen.get_width() + self.image.get_width()):
            self.delete_self()
