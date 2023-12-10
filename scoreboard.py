import pygame

FONT = "Font/GrinchedRegular.otf"
FONT_SIZE = 50
FONT_COLOR = (255, 255, 240)

SCOREBOARD_POSITION = (750, 550)


class Scoreboard:
    def __init__(self, screen):
        self.score = 0
        self.screen = screen
        self.game_font = pygame.font.Font(FONT, FONT_SIZE)

    def draw_scoreboard(self):
        score_surface = self.game_font.render(str(self.score), True, FONT_COLOR)
        self.screen.blit(score_surface, SCOREBOARD_POSITION)

    def update_score(self):
        self.score += 1

    def game_over(self):
        # Game Over text
        game_over = self.game_font.render(str(f"GAME OVER"), True, FONT_COLOR)
        game_over_rect = game_over.get_rect(center=(400, 100))
        self.screen.blit(game_over, game_over_rect)

        # Final score text
        final_score = self.game_font.render(str(f"Your score is {self.score}"), True, FONT_COLOR)
        final_score_rect = final_score.get_rect(center=(400, 200))
        self.screen.blit(final_score, final_score_rect)

        saved_score = self.update_highest_score()

        # Highest achieved score text
        highest_score = self.game_font.render(str(f"Highest Score: {saved_score}"), True, FONT_COLOR)
        highest_score_rect = highest_score.get_rect(center=(400, 400))
        self.screen.blit(highest_score, highest_score_rect)

    def update_highest_score(self):

        with open("highest_score.txt", "r+") as f:
            try:
                saved_score = int(f.read())
            except ValueError:
                saved_score = 0

        with open("highest_score.txt", "w") as f:
            if self.score > saved_score:
                f.write(str(self.score))
            else:
                f.write(str(saved_score))

        return saved_score

