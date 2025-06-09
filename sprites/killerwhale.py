import pygame, random
from sprites.dangerous_sprites import Dangerous

class KillerWhale(Dangerous):
    def __init__(self, screen: pygame.Surface, player, scene):
        super().__init__(screen, player, scene)
        
        self.image = pygame.image.load("./assets/killerwhale.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,
            (self.image.get_width() * 2,
            self.image.get_height() * 2)
        )

        self.fit_rect_size_to_image()

        self.rect.x = self.screen.get_width()
        height = self.screen.get_height()
        self.rect.y = random.randint(int(height / 8), int(height * (3 / 8)))


    def tick(self, delta_time):
        super().tick(delta_time)
        self.rect.x -= 1000 * delta_time
