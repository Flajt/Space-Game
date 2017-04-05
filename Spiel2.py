#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, pygame
from pygame.locals import *
import time
import random
from laser import *
import os
from kollision import *



class Spiel():

	def __init__(self, Display):
		self.display=Display
		self.display=pygame.display.set_mode((1500,1000))			#definiere Bilschirm + größe des Bildschirms
		pygame.display.set_caption("Star-Ship")
																#importiere alle Bilder und Rendert sie
		self.hintergrundbild=pygame.image.load("weltall.gif")
		self.hintergrund=pygame.transform.scale(self.hintergrundbild,(1500,1000))
		self.raumschiffbild=pygame.image.load("rakete.gif")
		self.raumschiff=pygame.transform.scale(self.raumschiffbild,(110,108))
		self.meteorbild=pygame.image.load("meteor.gif")
		self.meteorbild2=pygame.image.load("meteor.gif")
		self.meteor=pygame.transform.scale(self.meteorbild,(100,100))
		self.meteor2=pygame.transform.scale(self.meteorbild2,(100,100))
		self.alienbild=pygame.image.load("alien.gif")
		self.alien=pygame.transform.scale(self.alienbild,(100,100))


		# FPS festgesetzt
		self.Clock=pygame.time.Clock()
		self.FPS= 200



		self.laser_a=False		#setze alle notwendigen Variablen
		self.blau=(0,0,190)
		self.rot=(255,0,0)
		self.Weiss=(255,255,255)
		self.Gruen=(145,238,144)
		self.f=False
		self.x=200
		self.y=600
		self.u=0
		self.p=0
		self.q=-200
		self.player=3
		self.clock=time.clock()
		self.pos=(0,0)
		self.k=False
		self.raum=[]
		self.t=False
		self.m=False#FF0000
		self.Score=0
		self.richtung="keine"
		self.tastegedrueckt=False
		self.laser=Laser(self.blau,self.display) #bereite alles für Klassen nutzung vor
		self.alienlaser=Laser(self.rot,self.display)
		self.links=random.randint(10,900)	#generiere Zufallszahlen für meteroid eins und zwei
		self.zwei=random.randint(10,900)
		self.gesch=1.3
		self.altscore=self.Score
		self.Level=1
		self.zahl=0.5
		self.a=None




		count=random.randint(1,5)
		self.alien_x=[]
		self.alien_y=0
		for i in range(1,count+1):
				xcordinates=random.randint(1,1180)
				for i in self.alien_x:
					if xcordinates>=i-100 and xcordinates <=i+100:	#prüft ob die neuen x Koordinaten sich überlappen / gleich sind um 2 Schiffe auf einer Stelle sind
						c=True
						while c==True:
							xcordinates=random.randint(1,1180)
							for i in self.alien_x:
								if xcordinates>=i-100 and xcordinates <=i+100:
									c=True
									break
								else:
									c=False

				self.alien_x.append(xcordinates)

		self.m1=kollision(self.x,self.y,self.links,self.p,100)	#objekt zur Kollisionsabfrage für Raumschiff und Meteoriten
		self.m2=kollision(self.x,self.y,self.zwei,self.q,100)
		self.al=kollision(self.x, self.y,self.alien_x,self.alien_y,100)
		self.allaser=kollision(self.x,self.y,self.alienlaser.laser_1,self.alienlaser.laser_2,35)

		# ersten Laser für Alienraumschiffe

		for i in self.alien_x:
			self.alienlaser.laser_1.append(i)
			self.alienlaser.laser_2.append(self.alien_y+100)








	def aliens(self):			#funktion für alienraumschiffe
		count=random.randint(1,5)
		test_count=count
		self.alien_x=[]
		self.alien_y=0
		for i in range(1,count+1):
				xcordinates=random.randint(1,1180)
				for i in self.alien_x:
					if xcordinates>=i-100 and xcordinates <=i+100:	#prüft ob die neuen x Koordinaten sich überlappen / gleich sind um 2 Schiffe auf einer Stelle sind
						c=True
						while c==True:
							xcordinates=random.randint(1,1180)
							for i in self.alien_x:
								if xcordinates>=i-100 and xcordinates <=i+100:
									c=True
									break
								else:
									c=False
				self.alien_x.append(xcordinates)

	def main(self):							#definiere events
		self.Clock.tick(self.FPS)	#FPS werden "gestartet"
		self.display.blit(self.hintergrund,(0,0))
		for event in pygame.event.get():
			if event.type==QUIT:		#zum Fenster schließen
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:		#prüfe ob taste gedrückt wurde
				self.tastegedrueckt=True
				if event.key==pygame.K_LEFT:	#prüfe welche der Tasten gedrückt wurde
					self.richtung="links"
				if event.key==pygame.K_RIGHT:
					self.richtung="rechts"
				if event.key==pygame.K_UP:
					self.richtung="hoch"
				if event.key==pygame.K_DOWN:
					self.richtung="runter"
			else:
				self.tastegedrueckt=False		#wenn keine Taste gedrückt auf False setzen
			if event.type==pygame.MOUSEBUTTONDOWN:	#prüfe ob Mousetaste gedrückt wurde
				self.laser.laser_1.append(self.x)
				self.laser.laser_2.append(self.y)

	# hochrechnen um Laser fortzubewegen!
		i = 0
		while i<len(self.laser.laser_2):
			self.laser.laser_2[i] -= 1
			if self.laser.laser_2[i]<= -35:			#löscht letzten Wert der Listen damit nicht unnötig speicher verbraucht wird
				del(self.laser.laser_2[0])
				del(self.laser.laser_1[0])
			i = i+1

	# hochrechnen um Alienlaser fortzubewegen
		i = 0
		while i<len(self.alienlaser.laser_2):
			self.alienlaser.laser_2[i] += 1
			i = i+1


		if len(self.alienlaser.laser_2)>0:	#prüft ob
			if self.alienlaser.laser_2[0]>= 1100:	#prüft ob der Laser aus dem Bild geflogen ist
				self.alienlaser.laser_2=[]			#setze beide listen zurück
				self.alienlaser.laser_1=[]
				for i in self.alien_x:				# lässt aliens schießen sobald der laser aus dem Bild ist
					self.alienlaser.laser_1.append(i)
					self.alienlaser.laser_2.append(self.alien_y+100)





		if self.tastegedrueckt==True:		#prüft welche Pfeiltaste gedrückt wurde um das Schiff in die Richtung zu bewegen
			if self.richtung=="links" and self.x>0:
				self.x=self.x-1
			if self.richtung=="rechts" and self.x<1400:
				self.x=self.x+1
			if self.richtung=="hoch" and self.y>0:
				self.y=self.y-1
			if self.richtung=="runter" and self.y<900:
				self.y=self.y+1
													#definiere Zufallszahlen zum erzeugen der Meteoriden
		self.p=self.p+self.gesch
		if self.p>=1100:
			self.links=random.randint(10,900)
			self.p=0
			self.k=False

		self.q=self.q+self.gesch
		if self.q>=1100:
			self.zwei=random.randint(10,900)
			self.q=0
			self.k=False

#------------------------------------------------------------------------------#
#alien funktion

		if self.alien_y>=1100:	#lasse neue aliens Spawen sobald sie aus dem Bild sind
			self.aliens()




		while len(self.alien_x)==0:	#lässt alienschiffe erzeugen falls alle vernichtet worden sind
			self.aliens()


		for i in self.alien_x:	#zeichnet die Schiffe
			alien_form=pygame.Rect(i,self.alien_y,100,100)
			self.display.blit(self.alien,alien_form)

		self.alienlaser.schiessen(self.display)	#lässt alienlaser darstellen
		self.alien_y=self.alien_y+self.zahl		# und lässt ihn mit der vorgegeben Geschwindigkeit fliegen

		i=0
		while i<len(self.alien_x):				#alien kolisionsabfrage
			if self.al.getkollision(self.x,self.y,self.alien_x[i],self.alien_y,100)==True:
				del(self.alien_x[i])
				self.player=self.player-1
			i=i+1
#------------------------------------------------------------------------------#

							#zweite Kollisionsabfrage


		if self.m1.getkollision(self.x,self.y,self.links,self.p,100)==True:		#Kollisionsabfrage für Meteor 1 und 2 und Raumschiff
			self.links=random.randint(10,1180)	#setzt neue x Koordinaten fest
			self.player=self.player-1 #zieht ein Leben ab

		if self.m2.getkollision(self.x,self.y,self.zwei,self.q,100)==True:
			self.zwei=random.randint(10,1180)
			self.player=self.player-1


		for i in range(len(self.laser.laser_1)):	#große Kollisionsabfrage für Laser + Meteoriten
				if self.laser.laser_1[i]>self.zwei-5 and self.laser.laser_1[i]<self.zwei+100 and self.laser.laser_2[i]>self.q and self.laser.laser_2[i]<self.q+100:
					self.Score=self.Score+10 #rechnet 10 punkte auf den aktuellen
					self.zwei=random.randint(1,1180)
					self.q=0	#setzt
					# lasse meteor neu spawnen
				if self.laser.laser_1[i]>self.links and self.laser.laser_1[i]<self.links+100 and self.laser.laser_2[i]>self.p and self.laser.laser_2[i]<self.p+100:
					self.Score=self.Score+10
					self.links=random.randint(1,1180)
					self.p=0
				if self.laser.laser_1[i]+100>self.zwei-5 and self.laser.laser_1[i]+100<self.zwei+100 and self.laser.laser_2[i]>self.q and self.laser.laser_2[i]<self.q+100:
					self.Score=self.Score+10
					self.zwei=random.randint(1,1180)
					self.q=0
					# lasse meteor neu spawnen
				if self.laser.laser_1[i]+100>self.links and self.laser.laser_1[i]+100<self.links+100 and self.laser.laser_2[i]>self.p and self.laser.laser_2[i]<self.p+100:
					self.Score=self.Score+10
					self.links=random.randint(1,1180)
					self.p=0
					# lasse meteor neu spawnen




		for i in range(len(self.laser.laser_1)): # hier die abfrage für Spiellaser und alienschiffe
			j = 0
			while j < len(self.alien_x):
				if self.laser.laser_1[i]>self.alien_x[j]-5 and self.laser.laser_1[i]<self.alien_x[j]+100 and self.laser.laser_2[i]>self.alien_y and self.laser.laser_2[i]<self.alien_y+100:
						self.Score=self.Score+5
						del(self.alien_x[j])
				elif self.laser.laser_1[i]+100>self.alien_x[j]-5 and self.laser.laser_1[i]+100<self.alien_x[j]+100 and self.laser.laser_2[i]>self.alien_y and self.laser.laser_2[i]<self.alien_y+100:
						self.Score=self.Score+5 #addiert 5 Punkte auf den Punktestand
						del(self.alien_x[j]) #löscht das alienschiff das getroffen wurde
				j = j+1

		i=0
		while i<len(self.alienlaser.laser_1):		#kollisionsabfrage für alienlaser und Raumschiff
			if self.allaser.getkollision(self.x,self.y,self.alienlaser.laser_1[i],self.alienlaser.laser_2[i],35)==True:
				self.player=self.player-1
				del(self.alienlaser.laser_1[i]) #löscht alienlaser der Getroffen hat
				del(self.alienlaser.laser_2[i])
			i=i+1


		if self.Score>=self.altscore+50 :	#fügt level hinzu die die Geschwindigkeit erhöhen
			self.gesch=self.gesch+0.2
			self.altscore=self.Score		#speichert den aktuellen Score in der Altscore variable
			self.Level=self.Level+1
			self.zahl=self.zahl+0.2
			self.aliens()		#lässt aliens neu erscheinen





		rechteck=pygame.Rect(self.x,self.y,115,110) #x,y breite,laenge vom Raumschiff
		kreis=pygame.Rect(self.links,self.p,100,150)#erzeugt eim Rechteck mit Koordinaten von dem Darzustellendem und der Größe des Bildes
		kreiss=pygame.Rect(self.zwei,self.q,100,150)		#x y breite höhe (Für Laser Aufruf(laser1))
		self.laser.schiessen(self.display)#zeichet Laser
		self.display.blit(self.meteor,kreis) #meteor wird eingefuegt
		self.display.blit(self.raumschiff, rechteck) #raumschiffbild und das dafür zu nutzende Rechteck werden gezeichnet
		self.display.blit(self.meteor2, kreiss)

		pygame.font.init()				#initiert das "font" für die Leben
		myfont=pygame.font.SysFont("monospace", 20)		#lege größe und schriftart des auszugebenden Textes fest
		label = myfont.render("Leben:"+str(self.player), 1, (65,209,108))		#rendert Farbe + Text
		self.display.blit(label, (0, 100))						#legt Kordinaten (x, y) für den auszugebenden Text fest



		score=pygame.font.SysFont("monospace", 20)#defieniere schriftart und größe
		out_score=score.render("Score:"+str(self.Score),1,(65,209,108))# defieniere text aus in der Schriftfarbe
		self.display.blit(out_score,(0,175))# gibt alles an den x und y Koordinaten aus


		fps=pygame.font.SysFont("monospace", 20)#gibt FPS aus
		out_Fps=fps.render("FPS:"+str(self.FPS),1,(65,209,108))
		self.display.blit(out_Fps,(1400,5))

		stufe=pygame.font.SysFont("monospace", 20)#gibt level aus
		out_Stufe=fps.render("Level:"+str(self.Level),1,(65,209,108))
		self.display.blit(out_Stufe,(0,250))

		pygame.display.update()

		if self.player<=0 or self.player==0: #prüft die Spielerleben
			self.display.fill(self.rot)		#färbt das Display rot
			pygame.font.init()				# initallisiert ein Textfeld das gameover und den Punktestand ausgibt
			gameover=pygame.font.SysFont("monospace",100)
			out=gameover.render("GAME OVER",1,(15,6,6))
			out2=gameover.render("Ihr Score betraegt "+str(self.Score),1,(15,6,6))
			self.display.blit(out, (500,400))
			self.display.blit(out2, (150, 600))		#gibt den score wieder
			pygame.display.update()	#sorgt dafür das das Display auf den neusten stand gebracht wird
			time.sleep(5)
			return True	#gibt wieder ob man verloren hat und ins Menue zuruekgebracht werden soll
		else:
			return False
