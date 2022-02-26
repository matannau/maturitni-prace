import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.run_display = True
    
class MainMenu():
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            pass