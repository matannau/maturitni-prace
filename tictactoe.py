from gui.game import Game
from gui.menu import MainMenu, Settings, SuperMenu

mainmenu, settings, super = MainMenu(), Settings(), SuperMenu()

while super.running:
    while not mainmenu.display_menu():
        settings.display_settings()
    game = Game()
    game.game_loop(mainmenu.mode)
    while game.end_screen():
        game = Game()
        game.game_loop(mainmenu.mode)