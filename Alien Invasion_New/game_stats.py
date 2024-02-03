class GameStats():
    """Track the statistic of the game.
    
    <detailed version of the decription of the class. It could be multiple
    lines.>

    Attributes:
        level: int, the current level of the game.
        game_active: bool, if the game is active.
        ai_settings: Settings(), the settings of the game.
        ships_left: int, the number of ships left for the game.
    """

    def __init__(self, ai_settings):
        """Initialize the statistic.
        
        Arguments:
            ai_settings: Settings(), the initial settings of the game.
        """
        self.ai_settings = ai_settings
        self.reset_stats()

        # The game is active when it is lanched.
        self.game_active = True

    def reset_stats(self):
        """Initialize the possible change statistic during running the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.level = 1