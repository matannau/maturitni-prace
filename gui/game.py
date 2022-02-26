from json import load
import pygame
import math
import sys
from src.gui_func import create_points_horizontal, create_points_vertical, load_grid, place_symbol
from src.bot import check_if_computer, find_best_move_value, get_move, find_primary_value, need_to_block
from src.grid import create_grid
from src.wincheck import check_win


cross_image = pygame.image.load("resources/images/cross.png")
circle_image = pygame.image.load("resources/images/circle.png")
win_cross_image = pygame.image.load("resources/images/win_cross.png")
win_circle_image = pygame.image.load("resources/images/win_circle.png")

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing, self.end = True, False, False
        self.WHITE = (255, 255, 255)
        self.GREY = (192, 192, 192)
        self.BLACK = (0, 0, 0)
        self.WINDOW_SIZE = 500
        self.SURFACE = pygame.display.set_mode((self.WINDOW_SIZE, self.WINDOW_SIZE))
        self.gamegrid, self.size = create_grid(15)
        self.FPS = 5
        self.CLOCK = pygame.time.Clock()
        self.player, self.computer = "O", "X"
        self.players_turn = True
        self.computer_first, self.computer_second  = True, False
        self.win = False
        self.difficulty = 3
        self.font = pygame.font.Font("resources/acknowtt.ttf", int(self.WINDOW_SIZE/8))

    
    def draw_surface(self):
        self.SURFACE.fill(self.WHITE)
        start1, end1 = create_points_vertical(self.WINDOW_SIZE, self.size)
        start2, end2 = create_points_horizontal(self.WINDOW_SIZE, self.size)
        LINE_WIDTH = 1

        for i in range(self.size - 1):
            pygame.draw.line(self.SURFACE, self.GREY, start1[i], end1[i], LINE_WIDTH)
            pygame.draw.line(self.SURFACE, self.GREY, start2[i], end2[i], LINE_WIDTH)

    def draw_symbol(self, image, x, y):
        diameter = self.WINDOW_SIZE/self.size
        center = (diameter * (x + 1) - diameter/2, diameter * (y + 1) - diameter/2)
        image = pygame.transform.scale(image, (diameter - diameter/10, diameter - diameter/10))
        image_rect = image.get_rect()
        image_rect.center = center

        self.SURFACE.blit(image, image_rect)
    
    def draw_end_screen(self, symbol, winning_line):
        self.draw_winning_line(symbol, winning_line)
        win_text = self.font.render(f" {symbol} has won ", True, self.WHITE, self.BLACK)
        win_text_rect = win_text.get_rect()
        win_text_rect.center = (self.WINDOW_SIZE//2, self.WINDOW_SIZE//2)

        self.SURFACE.blit(win_text, win_text_rect)
    
    def draw_winning_line(self, symbol, winning_line):
        for item in winning_line:
            if symbol == "O":
                self.draw_symbol(win_circle_image, item[1], item[0])
                pygame.display.update()
                pygame.time.delay(100)
            else:
                self.draw_symbol(win_cross_image, item[1], item[0])
                pygame.display.update()
                pygame.time.delay(100)
    

  
    def initial_move(self):
        x, y = find_primary_value(self.gamegrid, self.size, self.player)
        arr = get_move(x, y)
        place_symbol(self.gamegrid, self.computer, arr)
        if self.computer == "O":
            self.draw_symbol(circle_image, arr[1], arr[0])
        else:
            self.draw_symbol(cross_image, arr[1], arr[0])
    
    def player_move(self, coord):
        x, y = math.floor(coord[0]/(self.WINDOW_SIZE/self.size)), math.floor(coord[1]/(self.WINDOW_SIZE/self.size))
        if place_symbol(self.gamegrid, self.player, (y, x)):
            self.players_turn = False
            if self.player == "O":
                self.draw_symbol(circle_image, x, y)
            else:
                self.draw_symbol(cross_image, x, y)

    def computer_move(self):
        boolean, player_value, player_moves = need_to_block(
            self.gamegrid, self.size, self.computer, self.player, self.difficulty)
        computer_value, computer_moves = find_best_move_value(
            self.gamegrid, self.size, self.player, self.computer, self.difficulty)
        if boolean:
            if computer_value <= player_value:
                arr = get_move(computer_value, computer_moves)
            else:
                arr = get_move(player_value, player_moves)
        else:
            arr = get_move(computer_value, computer_moves)

        print(f"player: {player_value}, computer: {computer_value}")
        print(f"Computer has chosen: {arr}")

        place_symbol(self.gamegrid, self.computer, arr)

        if self.computer == "O":
            self.draw_symbol(circle_image, arr[1], arr[0])
        else:
            self.draw_symbol(cross_image, arr[1], arr[0])


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                return True, (x, y)

        return False, []
        

    def game_loop(self):
        while self.playing:
            if self.computer_first:
                self.initial_move()
                self.computer_first = False
    
            while self.players_turn:
                clicked, coord = self.check_events()
                if clicked:
                    self.player_move(coord)
                    win, line = check_win(self.gamegrid, self.size)
                    if win:
                        self.draw_end_screen(win, line)

                self.CLOCK.tick(self.FPS)
                pygame.display.update()
            
            if self.computer_second:
                print("umbajaaa")
                self.initial_move()
                self.computer_second = False
            else:
                if self.playing:
                    self.computer_move()
                    win, line = check_win(self.gamegrid, self.size)
                    if win:
                        self.draw_end_screen(win, line)
                        self.playing = False

            self.players_turn = True
            pygame.display.update()
            self.CLOCK.tick(self.FPS)
    
    def end_screen(self):
        while self.end:
            self.check_events()
            self.CLOCK.tick(self.FPS)
