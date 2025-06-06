import pygame
from scenes.scene import Scene
from sprites.player_sprite import PlayerSprite
from sprites.background_sprite import BackgroundSprite
from sprites.tropical_fish_sprite import TropicalFish
from sprites.score_text import ScoreText
from sprites.shark_sprite import Shark

class PlayScene(Scene):
    mini_fish_timer = 0
    shark_timer = 0
    score = 0

    def init(self):
        self.player = PlayerSprite(self.screen)
        self.scene_number = 1
        self.sprites.append(BackgroundSprite(self.screen))
        self.sprites.append(self.player)
        self.sprites.append(TropicalFish(self.screen, self.player))
        self.sprites.append(ScoreText(self.screen, self.player))

    def tick(self, delta_time):
        super().tick(delta_time)

        self.mini_fish_timer += 1
        if self.mini_fish_timer > 100:
            self.sprites.append(TropicalFish(self.screen, self.player))
            self.mini_fish_timer = 0

        self.shark_timer += 1
        if self.shark_timer > 500:
            self.sprites.append(Shark(self.screen, self.player, self))
            self.shark_timer = 0

    def render(self):
        super().render()
