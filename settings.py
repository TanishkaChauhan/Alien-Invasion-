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
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

#         values that need to be changed as the game is played
        self.speedup_scale=1.1

        self.initialize_dynamic_settings()

        # setting the based down for level 1

    def initialize_dynamic_settings(self):
        self.ship_speed=1.5
        self.bullet_speed=2.5
        self.alien_speed=1
        self.fleet_direction=1

    def increase_speed(self):
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale

