import pygame
from sprites.sprite import Sprite

class Dangerous(Sprite):
    def __init__(self, screen, player, scene):
        super().__init__(screen)
        self.player = player
        self.scene = scene

    def tick(self, delta_time):
        if pygame.Rect.colliderect(self.get_hitbox(), self.player.get_hitbox()):
            self.scene.scene_number = 0
