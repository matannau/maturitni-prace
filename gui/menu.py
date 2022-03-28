import pygame
import sys
import configparser
from . images_menu import *


class SuperMenu():
    def __init__(self):
        pygame.init()
        self.running = True

        # Setting up colors
        self.WHITE = (255, 255, 255)
        self.GREY = (200, 200, 200)
        self.BLACK = (0, 0, 0)

        # Setting up FPS
        self.FPS = 30
        self.CLOCK = pygame.time.Clock()

        # Setting up display
        self.DISPLAYS = pygame.display.get_desktop_sizes()
        self.WINDOW_SIZE = self.DISPLAYS[0][1] * 2/3
        self.SURFACE = pygame.display.set_mode(
            (self.WINDOW_SIZE, self.WINDOW_SIZE))

        # Setting up caption, icon and font
        pygame.display.set_caption("Tic-tac-toe")
        pygame.display.set_icon(pygame.image.load("resources/images/icon.png"))
        self.FONT = pygame.font.Font(
            "resources/acknowtt.ttf", int(self.WINDOW_SIZE/8))

        # Setting up config
        self.config = configparser.ConfigParser()
        self.config.read("resources/config.ini")

    def check_events(self):
        # A function to check events throughout the game
        # Only pushing the cross on the top bar and
        # mouse buttons are being checked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                return True, (x, y)

        return False, []

    def draw_button(self, image, hover, x, y, scale):
        # A function to draw buttons on the screen. The functions controls
        # if the mouse is hovering over a button. If yes, hover version
        # of the button is displayed otherwise normal version is.
        #
        # The function also returns if button was clicked
        clicked = False
        image, image_rect = self.get_rect_image(image, x, y, scale)
        hover, hover_rect = self.get_rect_image(hover, x, y, scale)

        pos = pygame.mouse.get_pos()
        if image_rect.collidepoint(pos):
            self.SURFACE.blit(hover, hover_rect)
            if pygame.mouse.get_pressed()[0]:
                clicked = True
                return clicked
        else:
            self.SURFACE.blit(image, image_rect)
        return clicked

    def get_rect_image(self, image, x, y, scale):
        # Gets a rectangle of an image, scales it and centers it
        center = (x, y)
        w = image.get_width()
        h = image.get_height()
        image = pygame.transform.scale(image, (int(w * scale), int(h*scale)))
        image_rect = image.get_rect()
        image_rect.center = center

        return image, image_rect

    def draw_background(self, image, x, y, scale):
        # A function to draw background on the screen
        image, image_rect = self.get_rect_image(image, x, y, scale)
        image_rect.topleft = (0, 0)
        self.SURFACE.blit(image, image_rect)

    def load_background(self, image, direction):
        # Creates and animation of the background based on the direction
        if direction == True:
            number = 125
        else:
            number = 25
        for _ in range(20):
            number -= direction * 5
            self.draw_background(image, 0, 0, 0.1 * (self.WINDOW_SIZE/number))
            pygame.display.update()
            self.CLOCK.tick(self.FPS + 30)


class MainMenu(SuperMenu):
    def __init__(self):
        super().__init__()
        self.run_mainmenu = True
        self.mode = 0

    def draw_tictactoe(self, image, x, y):
        # Displays Tic-tac-toe image
        scale = self.WINDOW_SIZE / 1000
        image, image_rect = self.get_rect_image(image, x, y, scale)
        self.SURFACE.blit(image, image_rect)

    def rectangle_animation(self, image, x, y):
        # Displays initial rectangle animation
        center = (x, y)
        w = image.get_width()
        h = image.get_height()
        hscale = self.WINDOW_SIZE/1000
        num = 20000
        for i in range(19):
            num -= 1000
            image = pygame.transform.scale(
                image, (int(w * self.WINDOW_SIZE/num), int(h * hscale)))
            image_rect = image.get_rect()
            image_rect.center = center

            self.SURFACE.blit(image, image_rect)
            pygame.display.update()
            self.CLOCK.tick(self.FPS)

    def display_rectangle(self):
        # A function to draw background and then display rectangle animation
        self.draw_background(BACKGROUND, 0, 0, 0.1 * (self.WINDOW_SIZE/125))
        self.rectangle_animation(
            RECTANGLE, self.WINDOW_SIZE/2, 1 * self.WINDOW_SIZE/4)

    def display_menu(self):
        # A function to display the main menu with clickable buttons
        self.draw_background(BACKGROUND, 0, 0, 0.1 * (self.WINDOW_SIZE/125))
        self.draw_tictactoe(TICTAC, self.WINDOW_SIZE/2, 1 * self.WINDOW_SIZE/4)

        while self.run_mainmenu:
            SCALE = 0.6 * (self.WINDOW_SIZE/700)
            X = self.WINDOW_SIZE/2
            self.check_events()
            if self.draw_button(PVSC_BUTTON, HOVER_PVSC_BUTTON, X, 45 * self.WINDOW_SIZE/100, SCALE):
                self.mode = 1
                return True
            if self.draw_button(PVSP_BUTTON, HOVER_PVSP_BUTTON, X, 57 * self.WINDOW_SIZE/100, SCALE):
                self.mode = 2
                return True
            if self.draw_button(SETTINGS_BUTTON, HOVER_SETTINGS_BUTTON, X, 69 * self.WINDOW_SIZE/100, SCALE):
                pygame.time.delay(200)
                return False
            if self.draw_button(EXIT_BUTTON, HOVER_EXIT_BUTTON, X, 81 * self.WINDOW_SIZE/100, SCALE):
                pygame.quit()
                sys.exit()
            pygame.display.update()
            self.CLOCK.tick(self.FPS)


class Settings(SuperMenu):
    def __init__(self):
        super().__init__()
        self.run_settings = True

    def display_text(self, str, x, y, size, middle):
        # A function that creates a rectangle with given text, centers it
        # and then copies it onto the screen
        center = (x, y)
        self.FONT = pygame.font.Font(
            "resources/acknowtt.ttf", int(self.WINDOW_SIZE/size))
        text = self.FONT.render(str, True, self.BLACK)
        text_rect = text.get_rect()
        if middle == True:
            text_rect.center = center
        else:
            text_rect.topleft = center

        self.SURFACE.blit(text, text_rect)

    def display_settings_text(self):
        # This function displays text onto the settings screen
        self.display_text("SETTINGS", self.WINDOW_SIZE /
                          2, self.WINDOW_SIZE/7, 8, True)
        self.display_text("Difficulty", self.WINDOW_SIZE/15,
                          3 * self.WINDOW_SIZE/11, 22, False)
        self.display_text("Grid size", self.WINDOW_SIZE/15,
                          4.5 * self.WINDOW_SIZE/11, 22, False)
        self.display_text("Player symbol", self.WINDOW_SIZE /
                          15, 6 * self.WINDOW_SIZE/11, 22, False)

    def display_difficulty_buttons(self, scale):
        # A function to display adjustable difficulty options
        if not self.config["client"]["difficulty"] == "1":
            if self.draw_button(DIF1_BUTTON, HOVER_DIF1_BUTTON, 8 * self.WINDOW_SIZE/20, 29.5 * self.WINDOW_SIZE/100, scale):
                self.config["client"]["difficulty"] = "1"

        if not self.config["client"]["difficulty"] == "2":
            if self.draw_button(DIF2_BUTTON, HOVER_DIF2_BUTTON, 12.5 * self.WINDOW_SIZE/20, 29.5 * self.WINDOW_SIZE/100, scale):
                self.config["client"]["difficulty"] = "2"

        if not self.config["client"]["difficulty"] == "3":
            if self.draw_button(DIF3_BUTTON, HOVER_DIF3_BUTTON, 17 * self.WINDOW_SIZE/20, 29.5 * self.WINDOW_SIZE/100, scale):
                self.config["client"]["difficulty"] = "3"

    def display_grid_buttons(self, scale):
        # A function to display adjustable grid size options
        if not self.config["client"]["gridsize"] == "10":
            if self.draw_button(GRID10_BUTTON, HOVER_GRID10_BUTTON, 8 * self.WINDOW_SIZE/20, 43 * self.WINDOW_SIZE/100, scale):
                self.config["client"]["gridsize"] = "10"

        if not self.config["client"]["gridsize"] == "15":
            if self.draw_button(GRID15_BUTTON, HOVER_GRID15_BUTTON, 12.5 * self.WINDOW_SIZE/20, 43 * self.WINDOW_SIZE/100, scale):
                self.config["client"]["gridsize"] = "15"

        if not self.config["client"]["gridsize"] == "20":
            if self.draw_button(GRID20_BUTTON, HOVER_GRID20_BUTTON, 17 * self.WINDOW_SIZE/20, 43 * self.WINDOW_SIZE/100, scale):
                self.config["client"]["gridsize"] = "20"

    def display_symbol_buttons(self, scale):
        # A function to display adjustable symbol options
        if not self.config["client"]["playersymbol"] == "O":
            if self.draw_button(CIRCLE_BUTTON, HOVER_CIRCLE_BUTTON, 10.25 * self.WINDOW_SIZE/20, 56.75 * self.WINDOW_SIZE/100, scale):
                self.config["client"]["playersymbol"] = "O"
                self.config["client"]["computersymbol"] = "X"

        if not self.config["client"]["playersymbol"] == "X":
            if self.draw_button(CROSS_BUTTON, HOVER_CROSS_BUTTON, 14.75 * self.WINDOW_SIZE/20, 56.75 * self.WINDOW_SIZE/100, scale):
                self.config["client"]["playersymbol"] = "X"
                self.config["client"]["computersymbol"] = "O"

    def display_buttons(self):
        # A function to display all buttons onto the settings window
        # When SAVE button is clicked, config file is overwritten
        # When RESET button is clicked, settings are set to default
        # and then the config file is overwritten
        SCALE = 0.4 * (self.WINDOW_SIZE/700)
        if self.draw_button(SAVE_BUTTON, HOVER_SAVE_BUTTON, self.WINDOW_SIZE/3, 7 * self.WINDOW_SIZE/9, 0.5 * (self.WINDOW_SIZE/700)):
            with open("resources/config.ini", "w") as file:
                self.config.write(file)
            self.load_background(BACKGROUND, -1)
            return True

        if self.draw_button(RESET_BUTTON, HOVER_RESET_BUTTON, 2 * self.WINDOW_SIZE/3, 7 * self.WINDOW_SIZE/9, 0.5 * (self.WINDOW_SIZE/700)):
            self.config["client"]["playersymbol"] = self.config["DEFAULT"]["playersymbol"]
            self.config["client"]["computersymbol"] = self.config["DEFAULT"]["computersymbol"]
            self.config["client"]["gridsize"] = self.config["DEFAULT"]["gridsize"]
            self.config["client"]["difficulty"] = self.config["DEFAULT"]["difficulty"]
            with open("resources/config.ini", "w") as file:
                self.config.write(file)
            self.display_grey_buttons(0.4 * (self.WINDOW_SIZE/700))
            pygame.time.delay(200)

        self.display_difficulty_buttons(SCALE)
        self.display_grid_buttons(SCALE)
        self.display_symbol_buttons(SCALE)

    def display_grey_buttons(self, scale):
        # A function to display only hover version of the buttons
        self.draw_button(HOVER_DIF1_BUTTON, HOVER_DIF1_BUTTON, 8 *
                         self.WINDOW_SIZE/20, 29.5 * self.WINDOW_SIZE/100, scale)
        self.draw_button(HOVER_DIF2_BUTTON, HOVER_DIF2_BUTTON, 12.5 *
                         self.WINDOW_SIZE/20, 29.5 * self.WINDOW_SIZE/100, scale)
        self.draw_button(HOVER_DIF3_BUTTON, HOVER_DIF3_BUTTON, 17 *
                         self.WINDOW_SIZE/20, 29.5 * self.WINDOW_SIZE/100, scale)
        self.draw_button(HOVER_GRID10_BUTTON, HOVER_GRID10_BUTTON,
                         8 * self.WINDOW_SIZE/20, 43 * self.WINDOW_SIZE/100, scale)
        self.draw_button(HOVER_GRID15_BUTTON, HOVER_GRID15_BUTTON,
                         12.5 * self.WINDOW_SIZE/20, 43 * self.WINDOW_SIZE/100, scale)
        self.draw_button(HOVER_GRID20_BUTTON, HOVER_GRID20_BUTTON,
                         17 * self.WINDOW_SIZE/20, 43 * self.WINDOW_SIZE/100, scale)
        self.draw_button(HOVER_CIRCLE_BUTTON, HOVER_CIRCLE_BUTTON, 10.25 *
                         self.WINDOW_SIZE/20, 56.75 * self.WINDOW_SIZE/100, scale)
        self.draw_button(HOVER_CROSS_BUTTON, HOVER_CROSS_BUTTON, 14.75 *
                         self.WINDOW_SIZE/20, 56.75 * self.WINDOW_SIZE/100, scale)

    def display_settings(self):
        # This function displays the settings screen
        self.load_background(BACKGROUND, 1)
        self.display_settings_text()
        self.display_grey_buttons(0.4 * (self.WINDOW_SIZE/700))
        while self.run_settings:
            self.check_events()
            if self.display_buttons():
                return
            pygame.display.update()
            self.CLOCK.tick(self.FPS)
