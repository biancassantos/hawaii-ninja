import math

import pygame

from code.Constants import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, sprites_count: int):
        super().__init__(name, position)
        self.sprites_count = sprites_count
        self.current_sprite = 0

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

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
