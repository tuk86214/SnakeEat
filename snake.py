import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(200, 200), (210, 200), (220, 200)]
        self.direction = 'LEFT'

    def move(self):
        head = self.body[0]
        x, y = head

        if self.direction == 'UP':
            y -= GRID_SIZE
        elif self.direction == 'DOWN':
            y += GRID_SIZE
        elif self.direction == 'LEFT':
            x -= GRID_SIZE
        elif self.direction == 'RIGHT':
            x += GRID_SIZE

        # Boundary checks
        if x < 0:
            x = SCREEN_WIDTH - GRID_SIZE
        elif x >= SCREEN_WIDTH:
            x = 0
        if y < 0:
            y = SCREEN_HEIGHT - GRID_SIZE
        elif y >= SCREEN_HEIGHT:
            y = 0

        self.body.insert(0, (x, y))
        self.body.pop()

        return None
    
# Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - GRID_SIZE)
        self.y = random.randint(0, SCREEN_HEIGHT - GRID_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE))

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Create a snake object
snake = Snake()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 'DOWN':
                snake.direction = 'UP'
            elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                snake.direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                snake.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                snake.direction = 'RIGHT'

    # Move the snake
    snake.move()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the snake
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)  # 10 frames per second

pygame.quit()
sys.exit()

       



