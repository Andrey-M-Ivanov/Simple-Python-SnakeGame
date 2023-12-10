import pygame
from snake_body import Snake
from snake_food import SnakeFood
from scoreboard import Scoreboard

pygame.init()

CELL_SIZE = 20
WIDTH = 800
HEIGHT = 600
FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake_Game")

clock = pygame.time.Clock()

snake = Snake(screen)
food = SnakeFood(screen)
scoreboard = Scoreboard(screen)


def draw_background():
    green = (167, 209, 61)
    light_green = (175, 215, 70)

    screen.fill(light_green)

    x, y = 0, 0
    row = 0
    while y < HEIGHT:
        while x < WIDTH:
            pygame.draw.rect(screen, green, (x, y, CELL_SIZE, CELL_SIZE))
            x += CELL_SIZE * 2
        row += 1
        if row % 2 == 0:
            x = 0
        else:
            x = CELL_SIZE
        y += CELL_SIZE


def detect_collision_food(snake_head, current_food):
    if snake_head.rect.colliderect(current_food):
        snake.extend_snake()
        current_food.update_food_position()
        scoreboard.update_score()
        snake.play_crunch_sound()


def detect_collision_borders(snake_body):
    if snake_body.head.rect.x < 0 or snake_body.head.rect.x == WIDTH:
        scoreboard.game_over()
        return True
    if snake_body.head.rect.y < 0 or snake_body.head.rect.y == HEIGHT:
        scoreboard.game_over()
        return True


def detect_collision_snake_body(snake_body):
    current_seg = snake_body.head.next
    while current_seg is not None:
        if snake_body.head.rect.colliderect(current_seg.rect):
            scoreboard.game_over()
            return True
        current_seg = current_seg.next


def main():
    running = True
    snake_move_direction = "stop"
    game_over_state = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over_state:

            # Display graphics

            draw_background()
            food.draw_food()
            snake.draw_snake(snake_move_direction)
            scoreboard.draw_scoreboard()

            # Snake movement

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT] and snake_move_direction != "left" and snake_move_direction != "right":
                snake_move_direction = "right"
                snake.play_turn_sound()

            elif (keys[pygame.K_LEFT] and snake_move_direction != "right" and snake_move_direction != "left"
                    and snake_move_direction != "stop"):
                snake_move_direction = "left"
                snake.play_turn_sound()

            elif keys[pygame.K_UP] and snake_move_direction != "down" and snake_move_direction != "up":
                snake_move_direction = "up"
                snake.play_turn_sound()

            elif keys[pygame.K_DOWN] and snake_move_direction != "up" and snake_move_direction != "down":
                snake_move_direction = "down"
                snake.play_turn_sound()

            snake.move(snake_move_direction)

            # Collisions

            detect_collision_food(snake.head, food)
            if detect_collision_snake_body(snake):
                game_over_state = True
                snake.play_game_over()
            if detect_collision_borders(snake):
                game_over_state = True
                snake.play_game_over()

        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
