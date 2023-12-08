import pygame
import time


# Inicialization:
pygame.init()

# Screen:
widht = 1200
height = 700
screen = pygame.display.set_mode((widht, height))
distance = 3
fps = 60
clock = pygame.time.Clock()

# Colors:
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 125, 0)
blue = (0, 0, 255)
light_blue = (0, 150, 200)
yellow = (255, 255, 0)

# Title:
pygame.display.set_caption("Tanks Game")


def lines(lines_color):
    line_y = 70
    for line in range(0, 11):
        pygame.draw.line(screen, lines_color, (0, line_y), (1200, line_y))
        line_y += 70


# Image:
tank_image = pygame.image.load("img/tank.png")
tank_image_rect = tank_image.get_rect()
tank_image_rect.center = (widht//2, height//2)


# Main:
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Keyboarb:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and tank_image_rect.y > 0:
        tank_image_rect.y -= distance
    elif keys[pygame.K_DOWN] and tank_image_rect.y < height:
        tank_image_rect.y += distance
    elif keys[pygame.K_LEFT] and tank_image_rect.x > 0:
        tank_image_rect.x -= distance
    elif keys[pygame.K_RIGHT] and tank_image_rect.x < widht:
        tank_image_rect.x += distance

    screen.fill(light_blue)
    lines(red)
    # Input Image:
    screen.blit(tank_image, tank_image_rect)
    # Display Update:
    pygame.display.update()
    # Clock ticks:
    clock.tick(fps)

# Quit:
pygame.quit()

