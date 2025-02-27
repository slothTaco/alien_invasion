import pygame
from pygame.sprite import sprite

class Alien(sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(Self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        Self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        Self.image = pygame.image.load('images/alien.bmp')
        Self.rect = Self.image.get_rect()

        # Start eah new alien near the top left screen.
        Self.rect.x = Self.rect.width
        Self,rect,y = Self.rect.height

        #Store teh alien's exct horizontal position.
        Self.x = float(Self.rect.x)
