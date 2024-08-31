class Settings:
    """Stores all the settings for the game"""

    def __init__(self):
        """Initialize all game settings"""
        # Score settings
        self.score = 0
        self.score_rgb = (255, 255, 255)
        self.score_font = 'timenewroman'
        self.score_size = 40
        self.score_position = (190, 20)

        # Screen settings
        self.screen_width = 520
        self.screen_height = 570
        self.screen_rgb = (147, 197, 114)

        # Borders
        self.border_rgb = (79, 121, 66)
        self.top_border = (0, 0, 520, 60)
        self.bottom_border = (0, 560, 520, 10)
        self.left_border = (0, 0, 10, 570)
        self.right_border = (510, 0, 10, 570)
