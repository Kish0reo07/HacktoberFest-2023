import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong Game')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle settings
paddle_width, paddle_height = 15, 100
player1_x, player1_y = 50, (height - paddle_height) // 2
player2_x, player2_y = width - 50 - paddle_width, (height - paddle_height) // 2

# Ball settings
ball_size = 15
ball_x, ball_y = width // 2, height // 2
ball_x_velocity, ball_y_velocity = 5, 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= 5
    if keys[pygame.K_s] and player1_y < height - paddle_height:
        player1_y += 5
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 5
    if keys[pygame.K_DOWN] and player2_y < height - paddle_height:
        player2_y += 5

    # Move the ball
    ball_x += ball_x_velocity
    ball_y += ball_y_velocity

    # Bounce the ball off the top and bottom
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_y_velocity = -ball_y_velocity

    # Bounce the ball off the paddles
    if (ball_x <= player1_x + paddle_width and player1_y < ball_y < player1_y + paddle_height) or \
       (ball_x >= player2_x - ball_size and player2_y < ball_y < player2_y + paddle_height):
        ball_x_velocity = -ball_x_velocity

    # Reset the ball if it goes out of bounds
    if ball_x < 0 or ball_x > width:
        ball_x, ball_y = width // 2, height // 2
        ball_x_velocity = -ball_x_velocity

    # Fill the screen with black
    screen.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(screen, white, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (player2_x, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)

