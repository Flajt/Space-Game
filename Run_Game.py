import pygame
from Spiel2 import *

pygame.init()
weiss = (255, 255, 255)
rot = (190, 0, 0)
blau = (0, 0, 190)
gelb = (255,195,10)
schwarz = (0,0,0)
grau = (80,80,80)


Clock=pygame.time.Clock()
FPS= 200

groesse = 50
abstand = 5
menu = True
pos = 1
gameover = False

display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Space Adventure")
Spiel=Spiel(display)

myfont = pygame.font.SysFont("Comic Sans MS", 120)
labelUe = myfont.render("Space Adventure", 1,blau)
myfont = pygame.font.SysFont("Comic Sans MS", 90)
labelS = myfont.render("Spielen", 1, rot)
labelB = myfont.render("Beenden", 1, schwarz)


while True:
	Clock.tick(FPS)
	if menu == True:
		display.fill(grau)
		display.blit(labelUe, (520, 50))
		display.blit(labelS, (534, 350))
		display.blit(labelB, (520, 450))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if menu == True:
					if event.key == K_UP:
						if pos == 2:
							myfont = pygame.font.SysFont("Comic Sans MS", 90)
							labelS = myfont.render("Spielen", 1, rot)
							labelB = myfont.render("Beenden", 1, schwarz)
							pos = 1
					elif event.key == K_DOWN:
						if pos == 1:
							myfont = pygame.font.SysFont("Comic Sans MS", 90)
							labelS = myfont.render("Spielen", 1, schwarz)
							labelB = myfont.render("Beenden", 1, rot)
							pos = 2
					elif event.key == K_RETURN:
						if pos == 1:
							menu = False
						if pos==2:
							pygame.quit()
							sys.exit()
	if menu == False:
		gameover = Spiel.main()
		if gameover == True:
			menu = True
			Spiel.__init__(display)
	pygame.display.update()
