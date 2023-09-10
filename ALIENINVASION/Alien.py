import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent the individual alien and its features"""
    def __init__(self,ai_game):
        """Initialize the alien and set its start pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #load the alien image
        self.image = pygame.image.load('ALIENINVASION/images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each alien at its initial position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #update ship's original x coord
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_dir
        self.rect.x = self.x

    def check_edges(self):
        """return true if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
        
