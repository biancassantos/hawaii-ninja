import pygame
from pygame import Rect, Surface
from pygame.font import Font

from code.Constants import C_PINK, C_GREEN, MENU_OPTION, C_WINE, C_CREAM, MENU_TEXT_MARGIN, F_JETBRAINS_BOLD


class Menu:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load("./assets/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        #pygame.mixer_music.load("./assets/MenuTrack.wav")
        #pygame.mixer_music.play(-1)
        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(36, "Hawaii", C_PINK, (MENU_TEXT_MARGIN, 55))
            self.menu_text(48, "Ninja", C_GREEN, (MENU_TEXT_MARGIN, 95))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_WINE, (MENU_TEXT_MARGIN, 180 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_CREAM, (MENU_TEXT_MARGIN, 180 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # Move down menu options
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    # Move up menu options
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    # Select menu option
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font(F_JETBRAINS_BOLD, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
