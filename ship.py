import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self,ai_game):
        """ Initalize the ship and set its staring position"""
        self.screen= ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship bmp into to the game and get its rectangle (hit box)
        self.image= pygame.image.load('images/ship.bmp')
        self.rect= self.image.get_rect()

        # place the rectangle in which the ship is in,
        # in its starting position at the mid_bottom of the screen's rectangle
        self.rect.midbottom= self.screen_rect.midbottom

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """ Draw ship in position """
        self.screen.blit(self.image,self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1