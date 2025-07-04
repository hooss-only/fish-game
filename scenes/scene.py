import pygame

class Scene:
    sprites = []
    screen = None
    scene_number = 0
    
    def __init__(self, screen: pygame.Surface):
        self.sprites = []
        self.screen = screen
        self.scene_number = 0

    def init(self):
        return

    def render(self):
        for sprite in self.sprites:
            sprite.render()

    def tick(self, delta_time):
        for sprite in self.sprites:
            sprite.tick(delta_time)
        
        i = 0
        while i < len(self.sprites):
            if self.sprites[i].dead:
                del self.sprites[i]
                i -= 1
            i += 1

    def handle_event(self, event: pygame.event.Event, delta_time):
        for sprite in self.sprites:
            sprite.handle_event(event, delta_time)

    def get_scene_number(self):
        return self.scene_number
    
    def close(self):
        self.sprites = []
