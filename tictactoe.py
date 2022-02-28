from gui.game import Game
from gui.menu import MainMenu, Settings, SuperMenu
import pygame

pygame.init()
game = Game()
mainmenu, settings, super = MainMenu(), Settings(), SuperMenu()

while super.running:
    while mainmenu.display_menu():
        settings.display_settings()
    game.game_loop()
    while game.end_screen():
        game = Game()
        game.game_loop()
    game = Game()