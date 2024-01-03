import pygame
import random
import time

# Inicializácia:
pygame.init()

# Okno:
width = 1000
height = 550
screen = pygame.display.set_mode((width, height))
distance = 3
fps = 60
clock = pygame.time.Clock()

# Farby:
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 125, 0)
blue = (0, 0, 255)
light_blue = (0, 111, 225)
yellow = (255, 255, 0)
orange = (255, 170, 40)

# Score and Time:
Score = 0
HighestScore = 0
start_time = time.time()

# Nastavenie najvyššieho skóre zo súboru
try:
    with open("highest_score.txt", "r") as file:
        HighestScore = int(file.read())
except FileNotFoundError:
    pass

# Font:
game_text_font = pygame.font.SysFont("arial.ttf", 20)

# Názov:
pygame.display.set_caption("Hra s tankami")

Monster_list = [
    pygame.image.load("img/Monster1.png"),
    pygame.image.load("img/Monster2.png"),
    pygame.image.load("img/Monster3.png"),
    pygame.image.load("img/Monster4.png"),
    pygame.image.load("img/Monster5.png"),
    pygame.image.load("img/Monster6.png"),
]

# Enemies:
def monsters(position, monster_image):
    monster_image_rect = monster_image.get_rect()
    monster_image_rect.center = position
    screen.blit(monster_image, monster_image_rect)

enemy_speed = 1
position_x = 0
position_y = random.randint(50, height - 50)

MONSTER_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(MONSTER_EVENT, 5000)  # Čas v milisekundách, nastavte podle potřeby
monsters_list = []


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def boom(position):
    circles = []  # Prázdný seznam pro ukládání informací o kruzích
    radius = 3
    color = random_color()
    start_time = pygame.time.get_ticks()
    frames_per_second = 60  # Zvolte požadovanou rychlost animace

    for i in range(0, 10):
        circles.append((radius, color))  # Přidání informací o kruhu do seznamu
        radius += 3

    for i in range(10):
        # Klávesnica:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and tank_image_rect.y > 0:
            tank_image_rect.y -= distance
        elif keys[pygame.K_DOWN] and tank_image_rect.y < height - tank_image_rect.height:
            tank_image_rect.y += distance
        elif keys[pygame.K_LEFT] and tank_image_rect.x > 0:
            tank_image_rect.x -= distance
        elif keys[pygame.K_RIGHT] and tank_image_rect.x < width - tank_image_rect.width:
            tank_image_rect.x += distance

        # Vykresli obraz:
        screen.fill(light_blue)

        for circle_info in circles:
            pygame.draw.circle(screen, circle_info[1], position, circle_info[0], 1)

        screen.blit(tank_image, tank_image_rect)

        # Aktualizuj displej:
        pygame.display.update()

        # Spomalte animaci na 30 snímků za sekundu
        clock.tick(frames_per_second)

    end_time = pygame.time.get_ticks()


# Obraz:
tank_image = pygame.image.load("img/tank.png")
tank_image_rect = tank_image.get_rect()
tank_image_rect.center = (width - width // 3, height // 2)

bullet_image = pygame.image.load("img/bullet.png")
bullet_image_rect = bullet_image.get_rect()
bullet_image_rect.center = (tank_image_rect.x, tank_image_rect.centery)


class Bullet:
    def __init__(self, position, length, speed):
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.length = length
        self.speed = speed

    def draw(self):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x -= self.speed
        self.length -= self.speed * 2


BOOM_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(BOOM_EVENT, 100)

# Stav:
projektily = []

# Hlavný cyklus:
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet((tank_image_rect.x, tank_image_rect.centery), 2500, 5)
                projektily.append(bullet)
                bullet_x = bullet.rect.x
                bullet_y = bullet.rect.y
        elif event.type == BOOM_EVENT:
            for projektil in projektily[:]:
                if projektil.length <= 0 or projektil.rect.x <= 0:
                    boom((projektil.rect.x, projektil.rect.y + projektil.rect.height // 2))
                    projektily.remove(projektil)
        elif event.type == MONSTER_EVENT:
            monster_image = random.choice(Monster_list)
            monsters_list.append({
                'position_x': 0,
                'position_y': random.randint(50, height - 50),
                'created_time': pygame.time.get_ticks(),
                'monster_image': monster_image
            })

    # Klávesnice:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and tank_image_rect.y > 0:
        tank_image_rect.y -= distance
    elif keys[pygame.K_DOWN] and tank_image_rect.y < height - tank_image_rect.height:
        tank_image_rect.y += distance
    elif keys[pygame.K_LEFT] and tank_image_rect.x > 0:
        tank_image_rect.x -= distance
    elif keys[pygame.K_RIGHT] and tank_image_rect.x < width - tank_image_rect.width:
        tank_image_rect.x += distance

    # Vykresli obraz:
    screen.fill(light_blue)

    # Time:
    current_time = time.time() - start_time
    minutes = int(current_time // 60)
    seconds = int(current_time % 60)
    time_text = f"Time: {minutes:02d}:{seconds:02d}"

    text = f"Score: {Score}           Highest Score: {HighestScore}           Time: {time_text}"
    game_text = game_text_font.render(text, True, white)
    screen.blit(game_text, (width//2 - 150, 10))

    for projektil in projektily[:]:
        projektil.draw()
        projektil.move()
        if projektil.length <= 0 or projektil.rect.x <= 0:
            boom((projektil.rect.x, projektil.rect.y + projektil.rect.height // 2))
            projektily.remove(projektil)

    # Detekce kolize mezi střelami a monstry
    for projektil in projektily:
        for monster in monsters_list[:]:
            monster_rect = monster['monster_image'].get_rect()
            monster_rect.center = (monster['position_x'], monster['position_y'])

            if projektil.rect.colliderect(monster_rect):
                # Kolize detekována, odstranění střely a monstra
                projektily.remove(projektil)
                monsters_list.remove(monster)
                boom((monster['position_x'], monster['position_y']))
                Score += 10

    for monster in monsters_list:
        position_x = monster['position_x']
        position_y = monster['position_y']
        monsters_created_time = monster['created_time']
        position_x += enemy_speed

        monster_image = monster['monster_image']
        monster_image_rect = monster_image.get_rect()
        monster_image_rect.center = (position_x, position_y)

        if position_x >= width:
            monsters_list.remove(monster)
            Score -= 10
        else:
            monster['position_x'] = position_x
            monster_image = monster['monster_image']
            monsters((position_x, position_y), monster_image)

    screen.blit(tank_image, tank_image_rect)

    # Aktualizuj displej:
    pygame.display.update()

    # Hodiny:
    clock.tick(fps)

# Ukonči:
pygame.quit()

# Highest Score Save:
if Score >= HighestScore:
    HighestScore = Score
    with open("highest_score.txt", "w") as file:
        file.write(str(HighestScore))


