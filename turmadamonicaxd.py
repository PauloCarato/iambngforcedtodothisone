import pygame
from thiswillmakemyworkeasier import *
from enemieswhofly import *
from thingsfall import *

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
playerI= playercls('images/aicarumba.png',50,90,550,525)
vilain=enemy('images/ohno.png', 90,70,0,0)
bomb=things('images/bomba1.png',20,20,100,100)

fps = pygame.time.Clock()
running=True
while running:
    screen.blit(fundo, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
#player
    playerI.surja(screen)
    playerI.move(pygame.K_d,pygame.K_a)
#enemy
    vilain.surja(screen)
    vilain.voa()
#thingsfallin'
    bomb.surja(screen)
    bomb.cai()

    pygame.display.update()
    fps.tick(60)
    #paralax here

    #MAN I'M LOVING THAT SHIT WHAT
