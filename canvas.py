from player import Player 

class Canvas:
    def __init__(self, background_color):
        self.background_color = background_color

    def draw_background(self, screen):
        screen.fill(self.background_color)
        # Additional drawing code can be added here
    

