import pygame
import time

pygame.init()

# Screen:
	
width = 1080
height = 2340
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
bullet_speed = 5

# Farby:
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

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


bullets = []

bullet_cooldown = 0.22
last_shot_time = time.time() - bullet_cooldown

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
		  
    # Vkladanie obrazkov:
	
	screen.fill(white)
	screen.blit(scaled_image, scaled_image_rect)
	screen.blit(ship_image,ship_image_rect)
	
	# Vykteslenie bullet:
		
	for bullet in bullets:
		bullet.draw()
		
	
	
	# Update Obrazovky:
		
	pygame.display.update()
	
	clock.tick(fps)

pygame.quit()