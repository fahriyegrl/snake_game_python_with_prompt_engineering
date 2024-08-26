import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Snake settings
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Font
font = pygame.font.SysFont('arial', 25)

# Functions
def show_score(score):
    value = font.render(f"Score: {score}", True, WHITE)
    win.blit(value, [0, 0])

def game_over():
    message = font.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
    win.blit(message, [WIDTH // 6, HEIGHT // 3])
    pygame.display.flip()
    time.sleep(2)
    run_game()

def run_game():
    # Snake initial position and direction
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0
    snake_body = []
    snake_length = 1

    # Initial food position
    food_x = random.randint(0, (WIDTH // SNAKE_SIZE) - 1) * SNAKE_SIZE
    food_y = random.randint(0, (HEIGHT // SNAKE_SIZE) - 1) * SNAKE_SIZE

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -SNAKE_SIZE
                    dy = 0
                if event.key == pygame.K_RIGHT:
                    dx = SNAKE_SIZE
                    dy = 0
                if event.key == pygame.K_UP:
                    dx = 0
                    dy = -SNAKE_SIZE
                if event.key == pygame.K_DOWN:
                    dx = 0
                    dy = SNAKE_SIZE
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_c:
                    run_game()

        # Update snake position
        x += dx
        y += dy

        # Game over conditions
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over()

        # Snake body growth mechanism
        snake_head = [x, y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check for collision with itself
        for block in snake_body[:-1]:
            if block == snake_head:
                game_over()

        # Check if snake eats the food
        if x == food_x and y == food_y:
            food_x = random.randint(0, (WIDTH // SNAKE_SIZE) - 1) * SNAKE_SIZE
            food_y = random.randint(0, (HEIGHT // SNAKE_SIZE) - 1) * SNAKE_SIZE
            snake_length += 1

        # Draw everything
        win.fill(BLACK)
        for block in snake_body:
            pygame.draw.rect(win, GREEN, [block[0], block[1], SNAKE_SIZE, SNAKE_SIZE])

        pygame.draw.rect(win, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

        # Show score
        show_score(snake_length - 1)

        pygame.display.update()

        # Set the game speed
        clock.tick(SNAKE_SPEED)

# Start the game
run_game()
