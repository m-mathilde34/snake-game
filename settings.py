class Settings:
    """Stores all the settings for the game"""

    def __init__(self):
        """Initialize all game settings"""
        # Score settings
        self.score = 0

        # Screen settings
        self.screen_width = 500
        self.screen_height = 500
        self.screen_rgb = (128, 128, 128)