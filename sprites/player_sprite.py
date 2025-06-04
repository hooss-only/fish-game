import pygame
from sprites.sprite import Sprite

class PlayerSprite(Sprite):
    vx = 0; vy = 0
    width = 0; height = 0;

    movable = True
    horizontal = 1
    
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.image = pygame.image.load('./assets/fish.png').convert_alpha()
        self.image = pygame.transform.scale(
                self.image, 
                (self.image.get_width() * 0.1, 
                 self.image.get_height() * 0.1)
        )
        self.rect.x = 100; self.rect.y = 100
        self.fit_rect_size_to_image()

    def tick(self, delta_time):
        if self.movable:
            self.move_with_key(delta_time, 3000)
        self.detect_wall(delta_time)

        self.rect.x += self.vx * delta_time
        self.rect.y += self.vy * delta_time

    def move_with_key(self, delta_time, speed):
        keys = pygame.key.get_pressed()

        move_vertical = 0
        move_horizontal = 0

        if keys[pygame.K_a]:
            move_horizontal -= 1
        if keys[pygame.K_d]:
            move_horizontal += 1
        if keys[pygame.K_w]:
            move_vertical -= 1
        if keys[pygame.K_s]:
            move_vertical += 1

        self.vx += speed * move_horizontal * delta_time
        self.vy += speed * move_vertical * delta_time

        if move_horizontal != 0 and move_horizontal != self.horizontal:
            self.image = pygame.transform.flip(self.image, True, False)
            self.horizontal = move_horizontal

    def detect_wall(self, delta_time):
        screen_w, screen_h = self.screen.get_size()
        if (self.rect.x < 0 and self.vx < 0):
            self.vx = 0

        if (self.rect.x + self.rect.width > screen_w and self.vx > 0):
            self.vx = 0

        if (self.rect.y + self.rect.height / 2 < 0):
            self.vy += 5000 * delta_time;
            self.movable = False
        else:
            self.movable = True

        if (self.rect.y + self.rect.height > screen_h and self.vy > 0):
            self.vy = 0
