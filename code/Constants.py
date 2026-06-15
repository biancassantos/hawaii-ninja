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
    "KunoichiShot": 2,
    "Jellyfish": 1,
    "JellyfishShot": 3,
    "Octopus": 2,
    "OctopusShot": 3,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Kunoichi': 300,
    'KunoichiShot': 1,
    'Jellyfish': 50,
    'JellyfishShot': 1,
    'Octopus': 60,
    'OctopusShot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Kunoichi': 1,
    'KunoichiShot': 25,
    'Jellyfish': 1,
    'JellyfishShot': 20,
    'Octopus': 1,
    'OctopusShot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Kunoichi': 0,
    'KunoichiShot': 0,
    'Jellyfish': 100,
    'JellyfishShot': 0,
    'Octopus': 125,
    'OctopusShot': 0,
}

ENTITY_SHOT_DELAY = {
    'Kunoichi': 20,
    'Jellyfish': 100,
    'Octopus': 100,
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