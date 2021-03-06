import pygame
import math
from src.gui_func import create_points_horizontal, create_points_vertical, place_symbol
from src.bot import find_best_move_value, get_move, find_primary_value, need_to_block
from src.grid import create_grid
from src.wincheck import check_win
from . menu import SuperMenu
from .images_game import *


class Game(SuperMenu):
    def __init__(self):
        super().__init__()

        # Loading data from config file
        self.player = self.config["client"]["playersymbol"]
        self.computer = self.config["client"]["computersymbol"]
        self.difficulty = int(self.config["client"]["difficulty"])
        self.size = int(self.config["client"]["gridsize"])

        # Setting up game grid
        self.gamegrid = create_grid(self.size)
        self.spots = self.size**2

        # Setting up rules
        self.playing, self.end = True, False
        self.player1_turn, self.player2_turn = True, False
        self.players_turn, self.computer_choice = True, None
        self.player1, self.player2 = "X", "O"
        self.win = False
        if self.difficulty == 3:
            self.computer_first, self.computer_second = True, False
        else:
            self.computer_first, self.computer_second = False, True

    def draw_surface(self):
        # Draws a playing surface - a rectangle with size^2 spots
        self.SURFACE.fill(self.WHITE)
        start1, end1 = create_points_vertical(self.WINDOW_SIZE, self.size)
        start2, end2 = create_points_horizontal(self.WINDOW_SIZE, self.size)
        LINE_WIDTH = 1

        for i in range(self.size - 1):
            pygame.draw.line(self.SURFACE, self.GREY,
                             start1[i], end1[i], LINE_WIDTH)
            pygame.draw.line(self.SURFACE, self.GREY,
                             start2[i], end2[i], LINE_WIDTH)

    def draw_symbol(self, image, x, y):
        # Draws a cross or a circle on the playing surface with given coordinates
        diameter = self.WINDOW_SIZE/self.size
        center = (diameter * (x + 1) - diameter/2,
                  diameter * (y + 1) - diameter/2)
        image = pygame.transform.scale(
            image, (diameter - diameter/10, diameter - diameter/10))
        image_rect = image.get_rect()
        image_rect.center = center

        self.SURFACE.blit(image, image_rect)

    def draw_end_screen(self, symbol, winning_line):
        # Draws an ending screen stating who has won
        self.draw_winning_line(symbol, winning_line)
        if not symbol:
            win_text = self.FONT.render(
                f" It was a tie ", True, self.WHITE, self.BLACK)
        else:
            win_text = self.FONT.render(
                f" {symbol} has won ", True, self.WHITE, self.BLACK)
        win_text_rect = win_text.get_rect()
        win_text_rect.center = (
            self.WINDOW_SIZE/2, self.WINDOW_SIZE/2 - self.WINDOW_SIZE/10)

        self.SURFACE.blit(win_text, win_text_rect)

    def draw_winning_line(self, symbol, winning_line):
        # Creates a winning animation
        for item in winning_line:
            if symbol == "O":
                self.draw_symbol(WIN_CIRCLE_IMAGE, item[1], item[0])
                pygame.display.update()
                pygame.time.delay(100)
            else:
                self.draw_symbol(WIN_CROSS_IMAGE, item[1], item[0])
                pygame.display.update()
                pygame.time.delay(100)

    def initial_move(self):
        # Computer chooses an initial move and then it is drawn on screen
        x, y = find_primary_value(self.gamegrid, self.size, self.player)
        arr = get_move(x, y, self.difficulty, False)
        place_symbol(self.gamegrid, self.computer, arr)
        self.computer_choice = arr
        if self.computer == "O":
            self.draw_symbol(CHOSEN_CIRCLE_IMAGE, arr[1], arr[0])
        else:
            self.draw_symbol(CHOSEN_CROSS_IMAGE, arr[1], arr[0])

    def player_move(self, coord, player):
        # If it is possible, places symbol with given coordinates in the game grid
        # and then draws in on screen
        x, y = math.floor(coord[0]/(self.WINDOW_SIZE/self.size)
                          ), math.floor(coord[1]/(self.WINDOW_SIZE/self.size))
        if place_symbol(self.gamegrid, player, (y, x)):
            self.players_turn = self.player1_turn = self.player2_turn = False
            if player == "O":
                self.draw_symbol(CIRCLE_IMAGE, x, y)
            else:
                self.draw_symbol(CROSS_IMAGE, x, y)

    def computer_move(self):
        # Computer checks if player is needs to be blocked, if yes, it compares
        # its values with player's. If player's values ale greater, it means that
        # computer will win first, therefore there is no need to block. If they are
        # smaller, it takes player's best moves as hiw own.
        #
        # Computer chooses one of the best moves and then it is drawn on the screen
        boolean, player_value, player_moves = need_to_block(
            self.gamegrid, self.size, self.computer, self.player, self.difficulty)
        computer_value, computer_moves = find_best_move_value(
            self.gamegrid, self.size, self.player, self.computer, self.difficulty)
        if boolean:
            if computer_value <= player_value:
                arr = get_move(computer_value, computer_moves,
                               self.difficulty, True)
            else:
                arr = get_move(player_value, player_moves,
                               self.difficulty, False)
        else:
            arr = get_move(computer_value, computer_moves,
                           self.difficulty, True)

        print(f"player: {player_value}, computer: {computer_value}")
        print(f"Computer has chosen: {arr}")

        self.computer_choice = arr
        place_symbol(self.gamegrid, self.computer, arr)

        if self.computer == "O":
            self.draw_symbol(CHOSEN_CIRCLE_IMAGE, arr[1], arr[0])
        else:
            self.draw_symbol(CHOSEN_CROSS_IMAGE, arr[1], arr[0])

    def player_vs_computer(self):
        # Game loop for player vs computer mode
        # While no one has won and the grid is not full,
        # player and computer take turns
        while self.playing and self.spots > 2:
            if self.computer_first:
                self.initial_move()
                self.computer_first = False

            while self.players_turn:
                clicked, coord = self.check_events()
                if clicked:
                    self.player_move(coord, self.player)
                    win, line = check_win(self.gamegrid, self.size)
                    if win:
                        self.win = True
                        self.playing = False

                self.CLOCK.tick(self.FPS)
                pygame.display.update()

            if self.computer_second:
                self.initial_move()
                self.computer_second = False
            else:
                if self.playing:
                    if self.computer == "O":
                        self.draw_symbol(
                            CIRCLE_IMAGE, self.computer_choice[1], self.computer_choice[0])
                    else:
                        self.draw_symbol(
                            CROSS_IMAGE, self.computer_choice[1], self.computer_choice[0])
                    self.computer_move()
                    win, line = check_win(self.gamegrid, self.size)
                    if win:
                        self.win = True
                        self.playing = False

            self.players_turn = True
            pygame.display.update()
            self.CLOCK.tick(self.FPS)
            self.spots -= 2
        if self.win:
            self.draw_end_screen(win, line)
            self.end = True
            self.playing
        else:
            self.draw_end_screen(False, [])
            self.end = True
        pygame.time.delay(250)

    def player_vs_player(self):
        # Game loop for player vs player mode
        # While no one has won and the grid is not full,
        # players take turns
        while self.playing and self.spots > 2:
            while self.player1_turn:
                clicked, coord = self.check_events()
                if clicked:
                    self.player_move(coord, self.player1)
                    win, line = check_win(self.gamegrid, self.size)
                    if win:
                        self.win = True
                        self.playing = False

                self.CLOCK.tick(self.FPS)
                pygame.display.update()
            self.player2_turn = True

            if not self.win:
                while self.player2_turn:
                    clicked, coord = self.check_events()
                    if clicked:
                        self.player_move(coord, self.player2)
                        win, line = check_win(self.gamegrid, self.size)
                        if win:
                            self.win = True
                            self.playing = False

                    self.CLOCK.tick(self.FPS)
                    pygame.display.update()
                self.player1_turn = True
            self.spots -= 2

        if self.win:
            self.draw_end_screen(win, line)
            self.end = True
            self.playing
        else:
            self.draw_end_screen(False, [])
            self.end = True
        pygame.time.delay(250)

    def game_loop(self, mode):
        # If game mode is set to 1 (1 player), player vs computer
        # is launched, otherwise player vs player is
        self.draw_surface()
        if mode == 1:
            self.player_vs_computer()
        else:
            self.player_vs_player()

    def end_screen(self):
        # Draws buttons on the screen until one of them is clicked
        while self.end:
            self.check_events()
            SCALE = 0.8 * (self.WINDOW_SIZE/700)
            Y = 2 * self.WINDOW_SIZE / 3
            if self.draw_button(PLAYAGAIN_IMAGE, HOVER_PLAYAGAIN_IMAGE, 1 * self.WINDOW_SIZE / 3, Y, SCALE):
                pygame.time.delay(250)
                return 1

            if self.draw_button(MAINMENU_IMAGE, HOVER_MAINMENU_IMAGE, 2 * self.WINDOW_SIZE / 3, Y, SCALE):
                pygame.time.delay(250)
                return 0

            pygame.display.update()
            self.CLOCK.tick(self.FPS)
