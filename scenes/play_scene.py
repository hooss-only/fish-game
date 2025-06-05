import pygame
from scenes.scene import Scene
from sprites.player_sprite import PlayerSprite
from sprites.background_sprite import BackgroundSprite
from sprites.tropical_fish_sprite import TropicalFish

class PlayScene(Scene):
    mini_fish_timer = 0
    score = 0

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.player = PlayerSprite(self.screen)
        self.scene_number = 1
        self.sprites.append(BackgroundSprite(self.screen))
        self.sprites.append(self.player)
        self.sprites.append(TropicalFish(self.screen, self.player))
    
    def tick(self, delta_time):
        super().tick(delta_time)

        self.mini_fish_timer += 1
        if self.mini_fish_timer > 100:
            self.sprites.append(TropicalFish(self.screen, self.player))
            self.mini_fish_timer = 0
