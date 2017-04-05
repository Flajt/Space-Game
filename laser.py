#encodeing=utf-8
import pygame

class Laser():
	def __init__(self, farbe, display):
		self.farbe=farbe
		self.laser_1=[]
		self.laser_2=[]
		self.display=display

	def setLaser(self,laser,laser2):
		self.laser_1=laser	#x Koordinaten
		self.laser_2=laser2	#y Koordinaten


	def schiessen(self, display):
		for co in range(len(self.laser_1)):
			pygame.draw.rect(self.display,self.farbe,(self.laser_1[co], self.laser_2[co],5,35),0)#Laser soll eingefügt werden
			pygame.draw.rect(self.display,self.farbe,(self.laser_1[co]+100, self.laser_2[co],5,35),0)#zweiter Laser wird hinzugefuegt und an die richtge Stelle gesetzt werden
