import sys
import pygame
from Settings import Settings
from ship import ship
from bullet import bullet
from Alien import Alien

class AlienInvasion:
    def __init__(self):
        """Initializing game assets and behaviours"""
        pygame.init()
        self.settings = Settings()
        self.display = pygame.display
        self.screen = self.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.display.set_caption('JalienS')
        self.clock = pygame.time.Clock()
        #"self.bg_color = self.settings.bg_color"
        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()


        self._create_fleet()

    def run(self):
        """METHOD FOR STARTING THE MAIN LOOP FOR FRAME LOADING CONTINUOUSLY"""
        while True:
            #watch for keyboard and mouse(onclick) events
            self._check_events()
            
            self.ship.update_ship()
            self.bullets.update()

            #bullet method helper below 
            self._update_bullet()
            #self._create_fleet()
            self._update_screen()
            self._update_alien()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                    

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

                    

    def _check_keydown_events(self,event):
            if event.key == pygame.K_RIGHT:
                #move ship to the right
                self.ship.m_right = True

            elif event.key == pygame.K_LEFT:
                #MOVE SHIP TO THE LEFT
                self.ship.m_left = True

            elif event.key == pygame.K_q:
                #quit
                sys.exit()
            
            elif event.key == pygame.K_SPACE:
                #firing bullets
                self._fire_bullet()


    def _check_keyup_events(self,event):
            if event.key == pygame.K_RIGHT:
                        self.ship.m_right = False
            elif event.key == pygame.K_LEFT:
                        self.ship.m_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:

            new_bullet = bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create an alien and keep adding aliens horizontally till no room left"""
        #spacing between aliens is one alien_width and one alien_height
        new_alien = Alien(self)
        alien_width, alien_height = new_alien.rect.size
        current_x, current_y = alien_width, alien_height
        

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_positon, y_positon):
            """Create an alien and place it in right coordinates"""
            new_alien = Alien(self)
            new_alien.x = x_positon
            new_alien.rect.x = x_positon
            new_alien.rect.y = y_positon
            self.aliens.add(new_alien)    




    def _update_bullet(self):
        """Updating positon of old bullets and also new ones"""
        self.bullets.update()

        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)



    def _update_screen(self):
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw()
        self.display.flip()

    def _update_alien(self):
        self.aliens.update()
        self._check_fleet_edge()

    def _check_fleet_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_dir *= -1


if __name__ == '__main__':
    #MAKE A GAME INSTANCE AND RUN IT
    ai = AlienInvasion()
    ai.run()

