import pygame, random
from scenes.scene import Scene
from sprites.player_sprite import PlayerSprite
from sprites.background_sprite import BackgroundSprite
from sprites.tropical_fish_sprite import TropicalFish
from sprites.score_text import ScoreText
from sprites.danger_sprite import DangerSprite
from sprites.shark_sprite import Shark
from sprites.killerwhale import KillerWhale

class PlayScene(Scene):
    mini_fish_timer = 0
    shark_timer = 0
    big_thing_timer = 0
    big_thing = None
    while_big_thing = False
    score = 0
    screen: pygame.Surface
    
    def __init__(self, screen):
        super().__init__(screen)

    def init(self):
        self.player = PlayerSprite(self.screen)
        self.scene_number = 1
        self.sprites.append(BackgroundSprite(self.screen))
        self.sprites.append(self.player)
        self.sprites.append(TropicalFish(self.screen, self.player))
        self.sprites.append(ScoreText(self.screen, self.player))

        self.big_things = ["Killer whale!"]

    def tick(self, delta_time):
        super().tick(delta_time)

        self.mini_fish_timer += 1
        if self.mini_fish_timer > 100:
            self.sprites.append(TropicalFish(self.screen, self.player))
            self.mini_fish_timer = 0

        self.shark_timer += 1
        if self.shark_timer > 500:
            if not self.while_big_thing:
                self.sprites.append(Shark(self.screen, self.player, self))
            self.shark_timer = 0

        self.big_thing_timer += 1
        if self.big_thing_timer == 1000:
            match random.choice(self.big_things):
                case "Killer whale!":
                    self.show_killerwhale()
            self.while_big_thing = True

    def show_killerwhale(self):
        self.big_thing = KillerWhale(self.screen, self.player, self)
        self.sprites.append(DangerSprite(self.screen, pygame.Rect(0, self.big_thing.rect.y, self.screen.get_width(), self.big_thing.rect.height), self))

    def showtime(self):
        self.while_big_thing = False
        self.big_thing_timer = 0
        self.sprites.append(self.big_thing)

    def render(self):
        super().render()
