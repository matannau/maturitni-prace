from gui.game import Game
from gui.menu import MainMenu
from gui.menu import SuperMenu

game = Game()
mainmenu = MainMenu()
super = SuperMenu()

while super.running:
    mainmenu.display_menu()
    game.game_loop()
    while game.end_screen():
        game = Game()
        game.game_loop()
    game = Game()