class Settings():
    """The class stores all the settings in the game "Alien Invasion"."""
    def __init__(self):
        """Initialize the static settings."""
        # Settings of screen.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Settings of the ship.
        self.ship_limit = 3

        # Settings of bullets.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Settings of aliens.
        self.fleet_drop_speed = 10

        # Accelerate the rhythm of the game by speed 1.1.
        self.speedup_scale = 1.1

        # The speed of aliens points.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize the settings which change with the game progresses."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.2
        
        # Fleet_direction = 1 mean move right.
        # Fleet_direction = -1 mean move left.
        self.fleet_direction = 1

        # Scores.
        self.alien_points = 50

    def increase_speed(self):
        """Increase the speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        



