class Settings:
    """Stores all the settings for the game"""

    def __init__(self):
        """Initialize all game settings"""
        # Score settings
        self.score = 0
        self.score_rgb = (0, 0, 0)
        self.score_font = 'timenewroman'
        self.score_size = 40
        self.score_position = (190, 20)

        # Screen settings
        self.screen_width = 500
        self.screen_height = 550
        self.screen_rgb = (255, 255, 255)

        #Borders
        self.border_rgb = (128, 128, 128)
        self.top_border = (0, 0, 550, 60)
        self.bottom_border = (0, 540, 550, 10)
        self.left_border = (0, 0, 10, 550)
        self.right_border = (490, 0, 10, 550)
