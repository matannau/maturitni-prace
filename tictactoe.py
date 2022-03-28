from gui.game import Game
from gui.menu import MainMenu, Settings, SuperMenu

mainmenu, settings, supermenu = MainMenu(), Settings(), SuperMenu()
mainmenu.display_rectangle()
while supermenu.running:
    while not mainmenu.display_menu():
        settings.display_settings()
    game = Game()
    game.game_loop(mainmenu.mode)
    while game.end_screen():
        game = Game()
        game.game_loop(mainmenu.mode)
