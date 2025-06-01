import pygame

class Scene:
    sprites = []
    screen = None
    
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def render(self):
        for sprite in self.sprites:
            sprite.render()

    def tick(self, delta_time):
        for sprite in self.sprites:
            sprite.tick(delta_time)

    def handle_event(self, event: pygame.event.Event, delta_time):
        for sprite in self.sprites:
            sprite.handle_event(event, delta_time)

