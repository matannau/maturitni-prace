import pygame
import sys

PVSP_BUTTON = pygame.image.load("resources/images/pvsp.png")
PVSC_BUTTON = pygame.image.load("resources/images/pvsc.png")
SETTINGS_BUTTON = pygame.image.load("resources/images/settings.png")
HOVER_PVSP_BUTTON = pygame.image.load("resources/images/hover_pvsp.png")
HOVER_PVSC_BUTTON = pygame.image.load("resources/images/hover_pvsc.png")
HOVER_SETTINGS_BUTTON = pygame.image.load("resources/images/hover_settings.png")
TICTAC = pygame.image.load("resources/images/tictactoe.png")
BACKGROUND = pygame.image.load("resources/images/bg_color.png")


class SuperMenu():
    def __init__(self):
        pygame.init()
        self.running = True
        self.FPS = 5
        self.WHITE = (255, 255, 255)
        self.GREY = (192, 192, 192)
        self.BLACK = (0, 0, 0)
        self.FPS = 30
        self.CLOCK = pygame.time.Clock()
        self.WINDOW_SIZE = 500
        self.SURFACE = pygame.display.set_mode(
            (self.WINDOW_SIZE, self.WINDOW_SIZE))
        self.font = pygame.font.Font(
            "resources/acknowtt.ttf", int(self.WINDOW_SIZE/8))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                return True, (x, y)

        return False, []

    def draw_button(self, image, hover, x, y, scale):
        clicked = False
        image, image_rect = self.get_rect_image(image, x, y, scale)
        hover, hover_rect = self.get_rect_image(hover, x, y, scale)

        pos = pygame.mouse.get_pos()
        if image_rect.collidepoint(pos):
            self.SURFACE.blit(hover, image_rect)
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                return clicked
        else:
            self.SURFACE.blit(image, image_rect)

        return clicked

    def get_rect_image(self, image, x, y, scale):
        center = (x, y)
        w = image.get_width()
        h = image.get_height()
        image = pygame.transform.scale(image, (int(w * scale), int(h*scale)))
        image_rect = image.get_rect()
        image_rect.center = center

        return image, image_rect

    def draw_surface(self):
        self.SURFACE.fill(self.BLACK)


class MainMenu(SuperMenu):
    def __init__(self):
        super().__init__()
        self.run_mainmenu = True
    
    def draw_tictactoe(self, image, x, y):
        scale = self.WINDOW_SIZE / 1000
        image, image_rect = self.get_rect_image(image, x, y, scale)
        self.SURFACE.blit(image, image_rect)
    
    def draw_background(self, image, x, y):
        scale = 0.1 * (self.WINDOW_SIZE/125)
        image, image_rect = self.get_rect_image(image, x, y, scale)
        image_rect.topleft = (0, 0)
        self.SURFACE.blit(image, image_rect)

    def display_menu(self):
        self.draw_background(BACKGROUND, 0, 0)
        while self.run_mainmenu:
            SCALE = 0.6 * (self.WINDOW_SIZE/700)
            X = self.WINDOW_SIZE/2
            self.check_events()
            self.draw_tictactoe(TICTAC, self.WINDOW_SIZE/2, 1 * self.WINDOW_SIZE/4)
            if self.draw_button(PVSC_BUTTON, HOVER_PVSC_BUTTON, X, 3 * self.WINDOW_SIZE/6, SCALE):
                return
            if self.draw_button(PVSP_BUTTON, HOVER_PVSP_BUTTON, X, 4 * self.WINDOW_SIZE/6, SCALE):
                pass
            if self.draw_button(SETTINGS_BUTTON, HOVER_SETTINGS_BUTTON, X, 5 * self.WINDOW_SIZE/6, SCALE):
                pass
            pygame.display.update()
            self.CLOCK.tick(self.FPS)


class Settings(SuperMenu):
    def __init__(self):
        super().__init__()
        self.run_settings = True

    def display_settings(self):
        self.draw_surface()
        while self.run_settings:
            self.check_events()
            pygame.display.update()
            self.CLOCK.tick(self.FPS)
