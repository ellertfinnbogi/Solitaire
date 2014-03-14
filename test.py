import pygame
import sys
from pygame.locals import *
import random

class Game:

	def __init__(self):
		pygame.init()


		self.screen = self.setDisplay()


	def setDisplay(self):

		x_dim = 800
		y_dim = 600
		return pygame.display.set_mode((x_dim, y_dim)) 

	def getBackground(self):
		return pygame.image.load("background.jpg")

	def getBackgroundRect(self):

		return self.getBackground().get_rect()	

	def gameLoop(self):


		while True:

			for event in pygame.event.get():


				if(event.type == pygame.QUIT):
					pygame.quit()
					sys.exit()


			self.screen.blit(self.getBackground(),self.getBackgroundRect() )
		
			pygame.display.flip()
	

	def start(self):
		self.gameLoop()	


if __name__ =="__main__":
	g = Game()
	g.start()

