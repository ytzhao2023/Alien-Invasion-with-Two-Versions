class GameStats():
    """Track the statistic of the game."""
    def __init__(self, ai_settings):
        """Initialize the statistic."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # The game is active when it is lanched.
        self.game_active = False

        # Never reset the high score in any conditions.
        self.high_score = 0

    def reset_stats(self):
        """Initialize the possible change statistic during running the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1