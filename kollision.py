import pygame
import sys

class kollision():
	def __init__(self,x,y,x2,y2,laenge):
		self.x=x#z.B. x Koordinate Raumschiff
		self.y=y#z.B. y Koordinate Raumschiff
		self.x2=x2#z.B. x Koordinate Meteorit
		self.y2=y2#z.B. y Koordinate Meteorit
		self.laenge=laenge



	def getkollision(self,x,y,x2,y2,laenge):		#Funktion zur Kollisionsabfrage
		diff=0



		if x2>=x:
			diff=x2-x
		if x2<x:
			diff=x-x2



		diff2=0

		if y>=y2:
			diff2=y-y2
		if y<y2:
			diff2=y2-y



		if diff <=self.laenge and diff2 <=self.laenge+10:
			treffer=True
		else:
			treffer=False
		return treffer	#gibt treffer wieder
