from datetime import datetime

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import F_JETBRAINS_BOLD, C_PINK, SCORE_POS, MENU_OPTION, C_CREAM, C_WINE, C_GREEN
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load("./assets/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load("./assets/ScoreTrack.mp3")
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy("DBScore")
        name = ""
        while True:
            self.window.blit(self.surf, self.rect)
            self.score_text(48, "YOU WIN!", C_PINK, SCORE_POS['Title'])
            text = "Informe seu nome (4 caracteres):"
            character = ""
            if game_mode == MENU_OPTION[0]:
                character = "Kunoichi"
            self.score_text(18, text, C_CREAM, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name.upper(), 'score': player_score[0], 'character': character, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(18, name.upper(), C_CREAM, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load("./assets/ScoreTrack.mp3")
        pygame.mixer_music.play(-1)
        self.window.blit(self.surf, self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_GREEN, SCORE_POS['Title'])
        self.score_text(18, 'NAME     SCORE           DATE      ', C_PINK, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, character, date = player_score
            self.score_text(18, f'{name}     {score:05d}     {date}', C_CREAM,
                            SCORE_POS[list_score.index(player_score)])
        self.score_text(12, f"Pressione ESC para voltar", C_WINE,
                        SCORE_POS['GoBack'])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()
            pass

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font(F_JETBRAINS_BOLD, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"