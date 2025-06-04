import pygame
from scenes.scene import Scene
from sprites.player_sprite import PlayerSprite

class PlayScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.sprites.append(PlayerSprite(self.screen))
