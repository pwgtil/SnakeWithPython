import pygame

pygame.init()

CUBE_SIZE = 25
CUBES_NUM = 20
WIDTH = CUBES_NUM * CUBE_SIZE
screen = pygame.display.set_mode((WIDTH, WIDTH))
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screen.fill(WHITE)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


def draw_snake_part(x, y):
    position = (x * CUBE_SIZE,
                y * CUBE_SIZE,
                CUBE_SIZE,
                CUBE_SIZE)
    pygame.draw.rect(screen, GREEN, position)
    pygame.display.update()


def draw_food(x, y):
    radius = float(CUBE_SIZE) / 2
    position = (x * CUBE_SIZE + radius,
                y * CUBE_SIZE + radius)
    pygame.draw.circle(screen, BLUE, position)
