class Settings:
    """Stores all settings for the game"""

    def __init__(self):
        """Initialize all game settings"""
        # General
        self.game_font = 'arial'
        self.font_rgb = (255, 255, 255)
        self.font_size = 30
        self.title_rgb = (228, 208, 10)

        # Score settings
        self.score = 0
        self.score_size = 40

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

        # Game Over settings
        self.go_background = (0, 0, 0)
        self.go_font_size = 60

        # Start Screen settings
        self.ss_background = (79, 121, 66)
        self.title_size = 70
        self.credits_size = 15
