import pygame
from thiswillmakemyworkeasier import *
from enemyswhofly import *

#it will be bad

pygame.init()

    ###screen configs###
screen = pygame.display.set_mode((1200,650))
pygame.display.set_caption("famoso pega pega")
texto = pygame.font.SysFont("Comic_Sans", 20)
    #paralax
fundo=pygame.image.load('images/street.png')
#omg i love comic sans

    ###sprites###
playerI= playercls('images/aicarumba.png',50,90,100,100)

fps = pygame.time.Clock()
running=True
while running:
    screen.blit(fundo, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
#player
    playerI.surja(screen)
    playerI.move(pygame.K_d,pygame.K_a,pygame.K_w,pygame.K_s,)

#enemy



    pygame.display.update()
    fps.tick(60)
    #paralax here
