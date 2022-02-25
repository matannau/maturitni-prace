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

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.WHITE = (255, 255, 255)
        self.GREY = (192, 192, 192)
        self.WINDOW_SIZE = 500
        self.SURFACE = pygame.display.set_mode((self.WINDOW_SIZE, self.WINDOW_SIZE))
        self.gamegrid, self.size = create_grid(10)
        self.FPS = 5
        self.CLOCK = pygame.time.Clock()
        self.player = "X"
        self.computer = "O"
        self.players_turn = True
        self.computer_first = False

    
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
    
    def initial_move(self):
        x, y = find_primary_value(self.gamegrid, self.size, self.player)
        arr = get_move(x, y)
        place_symbol(self.gamegrid, self.computer, arr)
        if self.computer == "O":
            self.draw_symbol(circle_image, x, y)
        else:
            self.draw_symbol(cross_image, x, y)


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
    
            while self.players_turn:
                clicked, coord = self.check_events()
                if clicked:
                    x, y = math.floor(coord[0]/(self.WINDOW_SIZE/self.size)), math.floor(coord[1]/(self.WINDOW_SIZE/self.size))
                    if place_symbol(self.gamegrid, self.player, (y, x)):
                        # self.players_turn = False
                        if self.player == "O":
                            self.draw_symbol(circle_image, x, y)
                        else:
                            self.draw_symbol(cross_image, x, y)


                self.CLOCK.tick(self.FPS)
                pygame.display.update()

            
            load_grid(self.gamegrid, self.size)
            pygame.display.update()
            self.CLOCK.tick(self.FPS)