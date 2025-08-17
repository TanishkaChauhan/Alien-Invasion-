import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self,ai_game):
        """ Initalize the ship and set its staring position"""
        self.screen= ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship bmp into to the game and get its rectangle (hit box)
        self.image= pygame.image.load('images/ship.bmp')
        self.rect= self.image.get_rect()

        # place the rectangle in which the ship is in,
        # in its starting position at the mid_bottom of the screen's rectangle
        self.rect.midbottom= self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """ Draw ship in position """
        self.screen.blit(self.image,self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        # the ship's x cooridinate is being updated not the rectange
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x