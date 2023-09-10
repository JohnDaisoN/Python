import pygame


class ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize ship settings and set is start position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship imagea and get its rect
        self.image = pygame.image.load('ALIENINVASION/images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each ship at the middlebottom pos
        self.rect.midbottom = self.screen_rect.midbottom

        #store a float for the ship's pos
        self.x = float(self.rect.x)

        #flag for updating rightside continuous mvmnt of ship
        self.m_right = False
        self.m_left = False

    def update_ship(self):
        if self.m_right:
            self.x += self.settings.ship_speed
        elif self.m_left:
            self.x -= self.settings.ship_speed

        #update ship's self.rect.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at the current position"""
        self.screen.blit(self.image, self.rect)
