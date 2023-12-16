import pygame
import time
import random

pygame.init()

# Screen:
	
width = 1080
height = 2340
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60

# Farby:
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Enemy:
	
class Enemy:
	def __init__(self, image, position, length,speed, lives):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = position
		self.length = length
		self.speed = speed
		self.lives = lives
		
	def draw_enemy(self):
		screen.blit(self.image, self.rect)
		
	def move_enemy(self):
		self.rect.y += self.speed
		self.length -= self.speed * 2
		
	def reduce_lives(self):
		self.lives -= 1
		return self.lives


# Bullets:
	
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
        self.rect.y -= self.speed
        self.length -= self.speed * 2

# Obrazky:
	
ship_image = pygame.image.load("/storage/emulated/0/Android/PyGame/Img/ship.png")
ship_image_rect = ship_image.get_rect()
ship_image_rect.centerx = width//2
ship_image_rect.centery = 2000

backround_image = pygame.image.load("/storage/emulated/0/Android/PyGame/Img/vesmir.jpeg")
scaled_image = pygame.transform.scale(backround_image, (1080, 2340))
scaled_image_rect = backround_image.get_rect()
scaled_image_rect.topleft = (0, 0)

bullet_image = pygame.image.load("/storage/emulated/0/Android/PyGame/Img/bullet-green-icon.png")

ufo = pygame.image.load("/storage/emulated/0/Android/PyGame/Img/UFO-icon.png")
ufo1 = pygame.image.load("/storage/emulated/0/Android/PyGame/Img/UFO.png")

enemies_image = [ufo, ufo1]

boss_image = pygame.image.load("/storage/emulated/0/Android/PyGame/Img/boss.png")

boom_image = pygame.image.load("/storage/emulated/0/Android/PyGame/Img/Explosion-icon.png")

def boom(image, position):
	boom_image_rect = image.get_rect()
	boom_image_rect.center = position
	screen.blit(image, boom_image_rect)
	
bullets = []

bullet_speed = 5
bullet_cooldown = 0.2
last_shot_time = time.time() - bullet_cooldown

enemies = []
enemy_speed = 2
enemy_lives = 5
enemy_cooldown = 2.5
enemy_boss_cooldown = 35
last_enemy_time = time.time() - enemy_cooldown
last_boss_time = time.time() - enemy_boss_cooldown
boss_lst = []

is_button_pressed = False

# Hlavný cyklus:
	
lets_continue = True

while lets_continue:
	current_time = time.time()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			lets_continue = False
		
		# Ovladanie:
	   
		if event.type == pygame.FINGERMOTION:
			touch_x = event.x * screen.get_height()		
			touch_y = event.y * screen.get_width()
			if touch_x > 610 and touch_x < width + 590:
				ship_image_rect.center = (touch_x - 600, touch_y +650)

		if event.type == pygame.FINGERDOWN:
			is_button_pressed = True
			
		if event.type == pygame.FINGERUP:
			is_button_pressed = False
						
	if is_button_pressed and current_time - last_shot_time > bullet_cooldown:
			bullet = Bullet((ship_image_rect.x + 60, ship_image_rect.y -15), 3000, 5)
			bullets.append(bullet)
			bullet_x = bullet.rect.x
			bullet_y = bullet.rect.y
			last_shot_time = current_time
			
	#Pohyb bullet:
		
	for bullet in bullets:
		  bullet.move()		
		  
	# Delete bullet:
		  
	bullets = [bullet for bullet in bullets if bullet.rect.y + bullet.length > 0]  
	
	# Vytvoření nového nepřítele, pokud je cooldown vypršený:
	  
	enemy_image = random.choice(enemies_image)
	
	if current_time - last_enemy_time > enemy_cooldown:
		enemy = Enemy(enemy_image, (random.randint(50, 1000), -50), 2500, enemy_speed, 5)
		enemies.append(enemy)
		last_enemy_time = current_time
	elif current_time - last_boss_time > enemy_boss_cooldown:
		boss = Enemy(boss_image, (random.randint(50, 1000), -50), 2500, 1, 20)
		boss_lst.append(boss)
		last_boss_time = current_time
	
	for bullet in bullets[:]:
		for enemy in enemies[:]:
			if enemy.rect.colliderect(bullet.rect):
				remaining_lives = enemy.reduce_lives()
				if remaining_lives <= 0:
					enemies.remove(enemy)
					boom(boom_image, enemy.rect.center)
				bullets.remove(bullet)
				
	for bullet in bullets[:]:
		for boss in boss_lst:
			if boss.rect.colliderect(bullet.rect):
				remaining_lives = boss.reduce_lives()
				bullets.remove(bullet)
				if remaining_lives <= 0:
					boss_lst.remove(boss)		

    # Pohyb nepřátel:
	for enemy in enemies:
		enemy.move_enemy()
		
	for boss in boss_lst:
			  boss.move_enemy()
			  
    # Vkladanie obrazkov:
	
	screen.fill(white)
	#screen.blit(boom_image, boom_image_rect)
	screen.blit(scaled_image, scaled_image_rect)
	screen.blit(ship_image,ship_image_rect)
	
	# Vykreslenie bullet:
		
	for bullet in bullets:
		bullet.draw()
		
    # Vykreslení nepřátel:
	for enemy in enemies:
		enemy.draw_enemy()
		
	for boss in boss_lst:
		boss.draw_enemy()
		
	
	
	# Update Obrazovky:
		
	pygame.display.update()
	
	clock.tick(fps)

pygame.quit()