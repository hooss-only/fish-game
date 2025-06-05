import pygame
from scenes.scene import Scene
from sprites.player_sprite import PlayerSprite
from sprites.background_sprite import BackgroundSprite

class PlayScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.scene_number = 1
        self.sprites.append(BackgroundSprite(self.screen))
        self.sprites.append(PlayerSprite(self.screen))
