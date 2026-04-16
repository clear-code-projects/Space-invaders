import pygame 

class Laser(pygame.sprite.Sprite):
	def __init__(self,pos,speed_y,screen_height,speed_x=0):
		super().__init__()
		self.image = pygame.Surface((4,20))
		self.image.fill('white')
		self.rect = self.image.get_rect(center = pos)
		self.speed_y = speed_y
		self.speed_x = speed_x
		self.height_y_constraint = screen_height

	def destroy(self):
		if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
			self.kill()
		if self.rect.x <= -50 or self.rect.x >= self.height_y_constraint + 50:
			self.kill()

	def update(self):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		self.destroy()
