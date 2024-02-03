class Settings():
    """The class stores all the settings in the game "Alien Invasion"."""
    def __init__(self):
        # Settings of screen.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Settings of the ship.
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Settings of bullets.
        self.bullet_speed_factor = 3
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Settings of aliens.
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet_direction = 1 mean move right.
        # Fleet_direction = -1 mean move left.
        self.fleet_direction = 1

