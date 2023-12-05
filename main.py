import pygame

# Inicialization:
pygame.init()

# Screen:
wight = 1200
height = 700
screen = pygame.display.set_mode((wight, height))

# Colors:
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 125, 0)
blue = (0, 0, 255)
light_blue = (0, 200, 255)
yellow = (255, 255, 0)

# Title:
pygame.display.set_caption("Tanks Game")
screen.fill(light_blue)

# Practise:


# Main:
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    pygame.display.update()

# Quit:
pygame.quit()
