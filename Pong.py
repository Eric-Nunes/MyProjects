import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 0.5
PADDLE_SPEED = 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Paddle dimensions
paddle_width = 10
paddle_height = 100

# Ball dimensions
ball_width = 10
ball_height = 10

# Paddle positions
left_paddle_x = 50
left_paddle_y = (HEIGHT - paddle_height) // 2
right_paddle_x = WIDTH - 50 - paddle_width
right_paddle_y = (HEIGHT - paddle_height) // 2

# Ball position
ball_x = (WIDTH - ball_width) // 2
ball_y = (HEIGHT - ball_height) // 2
ball_dx = BALL_SPEED * random.choice((1, -1))
ball_dy = BALL_SPEED * random.choice((1, -1))

# Scores
left_score = 0
right_score = 0

# Fonts
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_a] and left_paddle_y < HEIGHT - paddle_height:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - paddle_height:
        right_paddle_y += PADDLE_SPEED

    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collisions
    if ball_y <= 0 or ball_y + ball_height >= HEIGHT:
        ball_dy *= -1

    if ball_x <= left_paddle_x + paddle_width and left_paddle_y <= ball_y + ball_height <= left_paddle_y + paddle_height:
        ball_dx *= -1

    if ball_x + ball_width >= right_paddle_x and right_paddle_y <= ball_y + ball_height <= right_paddle_y + paddle_height:
        ball_dx *= -1

    if ball_x < 0:
        right_score += 1
        ball_x = (WIDTH - ball_width) // 2
        ball_y = (HEIGHT - ball_height) // 2
        ball_dx = BALL_SPEED
        ball_dy = BALL_SPEED * random.choice((1, -1))

    if ball_x > WIDTH:
        left_score += 1
        ball_x = (WIDTH - ball_width) // 2
        ball_y = (HEIGHT - ball_height) // 2
        ball_dx = -BALL_SPEED
        ball_dy = BALL_SPEED * random.choice((1, -1))

    # Clear the screen
    win.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(win, WHITE, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(win, WHITE, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(win, WHITE, (ball_x, ball_y, ball_width, ball_height))

    # Draw the scores
    left_text = font.render(f"Left: {left_score}", True, WHITE)
    right_text = font.render(f"Right: {right_score}", True, WHITE)
    win.blit(left_text, (20, 20))
    win.blit(right_text, (WIDTH - right_text.get_width() - 20, 20))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
