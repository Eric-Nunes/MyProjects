import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SNAKE_SIZE = 20
SNAKE_SPEED = 10
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position
snake_x = WIDTH // 2
snake_y = HEIGHT // 2

# Snake initial speed and direction
snake_dx = SNAKE_SIZE
snake_dy = 0

# Snake body (initially just the head)
snake_body = [(snake_x, snake_y)]

# Food initial position
food_x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
food_y = random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)

# Score
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT]:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            if keys[pygame.K_RIGHT]:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if keys[pygame.K_UP]:
                snake_dx = 0
                snake_dy = -SNAKE_SIZE
            if keys[pygame.K_DOWN]:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    # Move the snake
    snake_x += snake_dx
    snake_y += snake_dy
    snake_head = (snake_x, snake_y)

    # Check for collisions with the food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
        food_y = random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
        snake_body.append(snake_head)

    # Update the display
    win.fill(WHITE)
    for segment in snake_body:
        pygame.draw.rect(win, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.draw.rect(win, GREEN, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.update()

    # Check for collisions with the screen boundaries
    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        running = False

    # Check for collisions with itself
    if snake_head in snake_body[:-1]:
        running = False

    # Move the snake
    snake_body.append(snake_head)
    if len(snake_body) > score + 1:
        del snake_body[0]

    pygame.time.delay(100)

# Quit pygame
pygame.quit()
