class Settings:
    """Stores all the settings for the game"""

    def __init__(self):
        """Initialize all game settings"""
        # Score settings
        self.score = 0

        # Screen settings
        self.screen_width = 500
        self.screen_height = 500
        self.screen_rgb = (255, 255, 255)

        #Borders
        self.border_rgb = (128, 128, 128)
        self.top_border = (0, 0, 500, 10)
        self.bottom_border = (0, 490, 500, 10)
        self.left_border = (0, 0, 10, 500)
        self.right_border = (490, 0, 10, 500)
