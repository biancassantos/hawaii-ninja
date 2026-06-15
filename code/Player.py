import pygame.key
import math

from code.Constants import WIN_WIDTH, ENTITY_SPEED, CHARACTER_FLOOR_BASE, CHARACTER_JUMP_HEIGHT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple, sprites_count: int):
        super().__init__(name, position)
        self.sprites_count = sprites_count
        self.is_jumping = False
        self.has_jumped = False
        self.current_sprite = 0
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        self.surf = self.get_first_sprite()
        # Move forward
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            if math.ceil(self.current_sprite) < self.sprites_count - 1:
                self.current_sprite += 0.2
                self.surf = self.get_current_sprite()
            else:
                self.current_sprite = 0
                self.surf = self.get_first_sprite()
        # Move backwards
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            if math.floor(self.current_sprite) == 0:
                self.surf = self.get_first_sprite()
                self.current_sprite = self.sprites_count - 1
            else:
                self.current_sprite -= 0.2
                self.surf = self.get_current_sprite()
        # Jump
        if pressed_key[pygame.K_UP] and not self.is_jumping:
            self.rect.bottom -= CHARACTER_JUMP_HEIGHT[self.name]
            self.is_jumping = True
            self.has_jumped = True
        if self.is_jumping:
            self.surf = (pygame.image
                         .load(f"./assets/{self.name}Jump.png")
                         .convert_alpha())
        # Move back down
        if self.has_jumped and self.rect.bottom < CHARACTER_FLOOR_BASE:
            self.rect.bottom += 1
        else:
            self.is_jumping = False
            self.has_jumped = False
            self.rect.bottom = CHARACTER_FLOOR_BASE

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_SPACE]:
                return PlayerShot(f"{self.name}Shot", (self.rect.centerx, self.rect.centery - 8))
        return None

    def get_first_sprite(self):
        return (pygame.image
                 .load(f"./assets/{self.name}.png")
                 .convert_alpha())

    def get_current_sprite(self):
        return (pygame.image
                 .load(f"./assets/{self.name + str(math.ceil(self.current_sprite))}.png")
                 .convert_alpha())
