import pygame


# C
C_CREAM = (240, 241, 193)
C_GREEN = (59, 125, 79)
C_PINK = (239, 95, 102)
C_WINE = (82, 51, 63)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    "Level1Bg0": 0,
    "Level1Bg1": 1,
    "Level1Bg2": 2,
    "Level1Bg3": 3,
    "Level2Bg0": 0,
    "Level2Bg1": 2,
    "Level2Bg2": 1,
    "Level2Bg3": 2,
    "Level3Bg0": 0,
    "Level3Bg1": 1,
    "Level3Bg2": 2,
    "Level3Bg3": 1,
    "Kunoichi": 2,
    "KunoichiShot": 2,
    "Jellyfish": 1,
    "JellyfishShot": 3,
    "Octopus": 2,
    "OctopusShot": 3,
    "Gorgon": 2,
    "GorgonShot": 3,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level3Bg3': 999,
    'Kunoichi': 300,
    'KunoichiShot': 1,
    'Jellyfish': 50,
    'JellyfishShot': 1,
    'Octopus': 60,
    'OctopusShot': 1,
    "Gorgon": 100,
    "GorgonShot": 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Kunoichi': 1,
    'KunoichiShot': 25,
    'Jellyfish': 1,
    'JellyfishShot': 15,
    'Octopus': 2,
    'OctopusShot': 20,
    'Gorgon': 5,
    'GorgonShot': 30,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Kunoichi': 0,
    'KunoichiShot': 0,
    'Jellyfish': 100,
    'JellyfishShot': 0,
    'Octopus': 125,
    'OctopusShot': 0,
    'Gorgon': 200,
    'GorgonShot': 0,
}

ENTITY_SHOT_DELAY = {
    'Kunoichi': 20,
    'Jellyfish': 100,
    'Octopus': 100,
    'Gorgon': 80,
}

# F
F_JETBRAINS_BOLD = "./assets/JetBrainsMono-Bold.ttf"

# M
MENU_OPTION = ('Iniciar',
               'Score',
               'Sair',)
MENU_TEXT_MARGIN = 450

# S
SPAWN_TIME_ENEMY = {
    'Level1': 3000,
    'Level2': 2000,
    'Level3': 1500,
}

# T
TIMEOUT_LEVEL = {
    'Level1': 60000,
    'Level2': 40000,
    'Level3': 20000,
}
TIMEOUT_STEP = 100

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# C
CHARACTER_FLOOR_BASE = WIN_HEIGHT - 6
CHARACTER_JUMP_HEIGHT = {
    "Kunoichi": 40,
}

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 40),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             'GoBack': (WIN_WIDTH / 2, 310),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }