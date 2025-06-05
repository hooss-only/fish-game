import pygame
from sprites.sprite import Sprite

class ScoreText(Sprite):
    def __init__(self, screen: pygame.Surface, player):
        super().__init__(screen)
        self.font = pygame.font.SysFont(None, 50)
        self.score_text = self.font.render("Score: 0", True, (255, 255, 255))
        self.player = player
    
    def tick(self, delta_time):
        self.score_text = self.font.render(f"Score: {self.player.get_score()}", True, (255, 255, 255))

    def render(self):
        self.screen.blit(self.score_text, (10, 10))

