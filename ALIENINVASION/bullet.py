import pygame
from pygame.sprite import Sprite

class bullet(Sprite):

    def __init__(self,ai_game):
        """create a bullet at ship's current pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create bullet at origin an then update its current position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop

        #store bullet pos on a float
        self.y = float(self.rect.y)

    def update(self):
        #move bullets up the screen
        #update exaxct pos of bullet
        self.y -= self.settings.bullet_speed

        #update bullet rect pos
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

