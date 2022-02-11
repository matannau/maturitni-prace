import pygame
import sys
import math
from gui_func import create_points_horizontal, create_points_vertical, load_grid, place_symbol
from bot import find_best_move_value, get_move, find_primary_value, need_to_block
from grid import create_grid
from wincheck import check_win

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

LINE_WIDTH = 1

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SURFACE.fill(WHITE)
pygame.display.set_caption("Tic-tac-toe")

start1, end1 = create_points_vertical(WINDOW_WIDTH, WINDOW_HEIGHT)
start2, end2 = create_points_horizontal(WINDOW_WIDTH, WINDOW_HEIGHT)

for i in range(9):
    pygame.draw.line(SURFACE, BLACK, start1[i], end1[i], LINE_WIDTH)
    pygame.draw.line(SURFACE, BLACK, start2[i], end2[i], LINE_WIDTH)

font = pygame.font.SysFont("calibri", 64)

FPS = 5
clock = pygame.time.Clock()

gamegrid, size = create_grid(10)
place_symbol(gamegrid, "X", [3, 3])
x, y = find_primary_value(gamegrid, size, "X")
arr = get_move(x, y)
place_symbol(gamegrid, "O", arr)

pygame.display.update()

running = True
while running:
    players_move = True
    while players_move:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x, y = math.floor(x/(WINDOW_WIDTH/size)), math.floor(y/(WINDOW_HEIGHT/size))
                if place_symbol(gamegrid, "X", (y, x)):
                    players_move = False
        
        clock.tick(FPS)
    
    boolean, player_value, player_moves = need_to_block(gamegrid, size, "O", "X")
    computer_value, computer_moves = find_best_move_value(gamegrid, size, "X", "O")
    if boolean:
        if computer_value <= player_value:
            arr = get_move(computer_value, computer_moves)
        else:
            arr = get_move(player_value, player_moves)
    else:
        arr = get_move(computer_value, computer_moves)

    place_symbol(gamegrid, "O", arr)

    load_grid(gamegrid, size)
    
    pygame.display.update()

    if not check_win(gamegrid, size):
        running = False

symbol = check_win(gamegrid, size)
if symbol == 1:
    symbol = "X"
else:
    symbol = "O"
win_text = font.render(f"{symbol} has won", True, WHITE, BLACK)
win_text_rect = win_text.get_rect()
win_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SURFACE.blit(win_text, win_text_rect)

    pygame.display.update()

    clock.tick(5)

