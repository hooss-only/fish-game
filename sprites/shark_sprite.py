import pygame
import random
from sprites.dangerous_sprites import Dangerous

class Shark(Dangerous):
    def __init__(self, screen: pygame.Surface, player, scene):
        super().__init__(screen, player, scene)
        self.player = player
        self.scene = scene

        self.image = pygame.image.load('./assets/shark.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,
            (self.image.get_width() * 0.3,
            self.image.get_height() * 0.3)
        )

        self.fit_rect_size_to_image()

        self.speed = 1000
        self.direction = random.choice([-1, 1])

        self.rect.y = random.randint(0, screen.get_height() - self.rect.height)
        

        if self.direction == -1:
            self.rect.x = screen.get_width() + self.rect.width
        else:
            self.rect.x = -self.rect.width
            self.image = pygame.transform.flip(self.image, True, False)
    
    def tick(self, delta_time):
        super().tick(delta_time)
        self.rect.x += self.direction * self.speed * delta_time
