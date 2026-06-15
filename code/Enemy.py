import math

import pygame

from code.Constants import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, sprites_count: int):
        super().__init__(name, position)
        self.sprites_count = sprites_count
        self.current_sprite = 0
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if math.ceil(self.current_sprite) < self.sprites_count - 1:
            self.current_sprite += 0.05
            self.surf = (pygame.image
                         .load(f"./assets/{self.name + str(math.ceil(self.current_sprite))}.png")
                         .convert_alpha())
        else:
            self.current_sprite = 0
            self.surf = (pygame.image
                         .load(f"./assets/{self.name}.png")
                         .convert_alpha())

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(f"{self.name}Shot", (self.rect.centerx - 12, self.rect.centery))
        return None