import pygame


# C
C_CREAM = (240, 241, 193)
C_GREEN = (59, 125, 79)
C_PINK = (239, 95, 102)
C_WINE = (82, 51, 63)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    "Level1Bg0": 0,
    "Level1Bg1": 1,
    "Level1Bg2": 2,
    "Level1Bg3": 3,
    "Kunoichi": 2,
    "Jellyfish": 1,
    "Octopus": 2,
}

# M
MENU_OPTION = ('Iniciar',
               'Score',
               'Sair',)
MENU_TEXT_MARGIN = 450

# S
SPAWN_TIME_ENEMY = 8000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# C
CHARACTER_FLOOR_BASE = WIN_HEIGHT - 6
CHARACTER_JUMP_HEIGHT = {
    "Kunoichi": 40,
}