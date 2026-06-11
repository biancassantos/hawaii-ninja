import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import WIN_HEIGHT, C_CREAM, EVENT_ENEMY, SPAWN_TIME_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.entity_list.append(EntityFactory.get_entity("Kunoichi"))
        self.timeout = 20000
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME_ENEMY)

    def run(self):
        # pygame.mixer_music.load(f"./assets/{self.name}.wav")
        # pygame.mixer_music.play()
        clock = pygame.time.Clock()
        while True:
            clock.tick(60) # fps
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(("Jellyfish", "Octopus"))
                    self.entity_list.append((EntityFactory.get_entity(choice)))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_CREAM, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_CREAM, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_CREAM, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        font_path = "./assets/JetBrainsMono-Bold.ttf"

        text_font: Font = pygame.font.Font(font_path, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
