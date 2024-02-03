import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Mean a class of single alien."""
    def __init__(self, ai_settings, screen):
        """Initialize alien and set its original location."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load image of alien and set its rect attribute.
        self.image = pygame.transform.scale_by(
            pygame.image.load("./Images/alien.bmp"), 
                0.2)
        self.rect = self.image.get_rect()

        # Every alien's location are near the top left corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the precise location of alien.
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Draw the alien in pointed location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """If aliens locate in the edge of screen, then return True."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def update(self):
        """Move aliens right or left."""
        self.x += (self.ai_settings.alien_speed_factor * 
            self.ai_settings.fleet_direction)
        self.rect.x = self.x

        
