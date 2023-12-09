import pygame
import time


# Inicialization:
pygame.init()

# Screen:
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
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
light_blue = (0, 111, 225)
yellow = (255, 255, 0)

# Title:
pygame.display.set_caption("Tanks Game")


def lines(lines_color):
    line_y = 70
    for line in range(0, 11):
        pygame.draw.line(screen, lines_color, (0, line_y), (width - width//2, line_y))
        line_y += 70



def bullet(color, position):
    line_length = 650
    gap_length = 5
    current_pos = position

    while line_length > 0:
        pygame.draw.line(screen, color, current_pos, (current_pos[0] - gap_length, current_pos[1]))
        pygame.draw.line(screen, white, current_pos, (current_pos[0] - gap_length, current_pos[1]))
        pygame.time.delay(100)

        # Posun na další pozici
        current_pos = (current_pos[0] - gap_length * 2, current_pos[1])
        line_length -= gap_length * 2
        print(line_length)
        pygame.display.flip()


# Image:
tank_image = pygame.image.load("img/tank.png")
tank_image_rect = tank_image.get_rect()
tank_image_rect.center = (width - width//3, height//2)

#tank_position = (tank_image_rect.x, tank_image_rect.y)

# Main:
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(event)
                bullet(yellow, (tank_image_rect.x, tank_image_rect.y))
                print("test")
    # Keyboard:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and tank_image_rect.y > 0:
        tank_image_rect.y -= distance
    elif keys[pygame.K_DOWN] and tank_image_rect.y < height - tank_image_rect.height:
        tank_image_rect.y += distance
    elif keys[pygame.K_LEFT] and tank_image_rect.x > 0:
        tank_image_rect.x -= distance
    elif keys[pygame.K_RIGHT] and tank_image_rect.x < width - tank_image_rect.width:
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

