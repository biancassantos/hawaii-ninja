import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import C_CREAM, EVENT_ENEMY, SPAWN_TIME_ENEMY, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL, F_JETBRAINS_BOLD
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int], has_boss: bool = False):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.has_boss = has_boss
        self.timeout = TIMEOUT_LEVEL[self.name]
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(f"{self.name}Bg"))
        player = EntityFactory.get_entity("Kunoichi")
        player.score = player_score[0]
        self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME_ENEMY[self.name])
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        # pygame.mixer_music.load(f"./assets/{self.name}.wav")
        pygame.mixer_music.set_volume(0.3)
        # pygame.mixer_music.play()
        clock = pygame.time.Clock()
        while True:
            clock.tick(60) # fps
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shot = ent.shoot()
                    if shot is not None:
                        self.entity_list.append(shot)
                if ent.name == "Kunoichi":
                    self.level_text(14, f'Kunoichi - Health: {ent.health} | Score: {ent.score}', C_CREAM, (10, 22))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(("Jellyfish", "Octopus"))
                    if self.has_boss:
                        choice = random.choice(("Jellyfish", "Octopus", "Gorgon"))
                    self.entity_list.append((EntityFactory.get_entity(choice)))
                # End of level (timeout)
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                player_score[0] = ent.score
                        return True
                # End of level (no player)
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_CREAM, (10, 5))

            pygame.display.flip()
            # Collisions
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font(F_JETBRAINS_BOLD, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
