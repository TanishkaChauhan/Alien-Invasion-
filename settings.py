class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed= 1.5 # now the ship moves 1.5 pixels per cycle
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed=2.5
        # temp width
        self.bullet_width=300
        self.bullet_height=15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed =1.0
        self.fleet_drop_speed = 50
        self.fleet_direction = 1

