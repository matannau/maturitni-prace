from gui.game import Game

game = Game()

while game.running:
    game.playing = True

    game.draw_surface()
    game.game_loop()
    game.end = True
    game.end_screen()