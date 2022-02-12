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
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (192, 192, 192)

LINE_WIDTH = 1

WINDOW_SIZE = 400
SURFACE = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
SURFACE.fill(WHITE)
pygame.display.set_caption("Tic-tac-toe")

gamegrid, size = create_grid(15)
diameter = WINDOW_SIZE/size

start1, end1 = create_points_vertical(WINDOW_SIZE, size)
start2, end2 = create_points_horizontal(WINDOW_SIZE, size)

for i in range(size - 1):
    pygame.draw.line(SURFACE, GREY, start1[i], end1[i], LINE_WIDTH)
    pygame.draw.line(SURFACE, GREY, start2[i], end2[i], LINE_WIDTH)

font = pygame.font.SysFont("calibri", int(WINDOW_SIZE/9))

circle_image = pygame.image.load("images/circle.png")
circle_image = pygame.transform.scale(
    circle_image, (diameter - diameter/10, diameter - diameter/10))
circle_image_rect = circle_image.get_rect()
cross_image = pygame.image.load("images/cross.png")
cross_image = pygame.transform.scale(
    cross_image, (diameter - diameter/10, diameter - diameter/10))
cross_image_rect = cross_image.get_rect()


FPS = 5
clock = pygame.time.Clock()

computers_turn = True
not_computers_turn = False
win = False

player = "O"
computer = "X"

# Main game loop
running = True
while running:
    if computers_turn:
        x, y = find_primary_value(gamegrid, size, player)
        arr = get_move(x, y)

        place_symbol(gamegrid, computer, arr)

        center = (diameter * (arr[1] + 1) - diameter/2,
                  diameter * (arr[0] + 1) - diameter/2)
        cross_image_rect.center = center
        SURFACE.blit(cross_image, cross_image_rect)

        computers_turn = False

    pygame.display.update()

    players_turn = True
    while players_turn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x, y = math.floor(x/(WINDOW_SIZE/size)
                                  ), math.floor(y/(WINDOW_SIZE/size))
                if place_symbol(gamegrid, player, (y, x)):
                    players_turn = False
                    center = (diameter * (x + 1) - diameter/2,
                              diameter * (y + 1) - diameter/2)

                    circle_image_rect.center = center
                    SURFACE.blit(circle_image, circle_image_rect)

                    if check_win(gamegrid, size):
                        win = True

        clock.tick(FPS)
    

    if not_computers_turn:
        x, y = find_primary_value(gamegrid, size, player)
        arr = get_move(x, y)
        place_symbol(gamegrid, computer, arr)

        center = (diameter * (arr[1] + 1) - diameter/2,
                  diameter * (arr[0] + 1) - diameter/2)
        cross_image_rect.center = center
        SURFACE.blit(cross_image, cross_image_rect)

        not_computers_turn = False

    else:
        if not win:
            boolean, player_value, player_moves = need_to_block(
                gamegrid, size, computer, player)
            computer_value, computer_moves = find_best_move_value(
                gamegrid, size, player, computer)
            if boolean:
                if computer_value <= player_value:
                    arr = get_move(computer_value, computer_moves)
                else:
                    arr = get_move(player_value, player_moves)
            else:
                arr = get_move(computer_value, computer_moves)

            print(f"player: {player_value}, computer: {computer_value}")
            print(f"Computer has chosen: {arr}")

            place_symbol(gamegrid, computer, arr)

            center = (diameter * (arr[1] + 1) - diameter/2,
                    diameter * (arr[0] + 1) - diameter/2)
            cross_image_rect.center = center
            SURFACE.blit(cross_image, cross_image_rect)

    pygame.display.update()

    if check_win(gamegrid, size):
        symbol = check_win(gamegrid, size)
        if symbol == 1:
            symbol = "X"
        else:
            symbol = "O"
        win_text = font.render(f"{symbol} has won", True, WHITE, BLACK)
        win_text_rect = win_text.get_rect()
        win_text_rect.center = (WINDOW_SIZE//2, WINDOW_SIZE//2)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            SURFACE.blit(win_text, win_text_rect)

            pygame.display.update()

            clock.tick(5)
