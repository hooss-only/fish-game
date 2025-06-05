import pygame

class Sprite:
    rect = pygame.Rect(0, 0, 0, 0)
    dead = False
    screen: pygame.Surface
    image: pygame.Surface

    def __init__(self, screen: pygame.Surface):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.screen = screen
        self.dead = False

    def render(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def tick(self, delta_time):
        return

    def handle_event(self, event: pygame.event.Event, delta_time):
        return
    
    def fit_rect_size_to_image(self):
        self.rect.width, self.rect.height = self.image.get_size()

    def get_hitbox(self):
        return self.rect
    
    def delete_self(self):
        self.dead = True
