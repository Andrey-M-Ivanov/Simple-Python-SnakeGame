import pygame
from random import randint

IMAGE_SIZE = (20, 20)
CELL_SIZE = 20


class SnakeFood:

    def __init__(self, screen):
        self.screen = screen
        self.x = randint(0, self.screen.get_width()/CELL_SIZE - 1)
        self.y = randint(0, self.screen.get_height()/CELL_SIZE - 1)
        self.rect = pygame.Rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.apple = pygame.transform.scale(pygame.image.load("Graphics/apple.png").convert_alpha(), IMAGE_SIZE)

    def draw_food(self):
        self.screen.blit(self.apple, self.rect)
        # pygame.draw.rect(self.screen, "red", self.rect)

    def update_food_position(self):
        self.rect.x = randint(0, self.screen.get_width()/CELL_SIZE - 1) * CELL_SIZE
        self.rect.y = randint(0, self.screen.get_height()/CELL_SIZE - 1) * CELL_SIZE




