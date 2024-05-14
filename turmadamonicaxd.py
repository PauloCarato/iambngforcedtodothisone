import pygame
from thiswillmakemyworkeasier import *
from enemieswhofly import *
from thingsfall import *

point=0
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
# vilain=enemy('images/ohno.png', 90,70,0,0)
bomb= fall('images/bomba1.png',32,32)
soja= fall('images/soja.png',80,80)
objects1=[fall('images/bomba1.png',32,32),
          fall('images/bomba1.png',32,32),
          fall('images/bomba1.png',32,32),]

objects2=[fall('images/soja.png',80,80),
          fall('images/arroz.png',80,80),
          fall('images/milho.png',80,80),
          fall('images/trigo.png',80,80)]

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
    # vilain.surja(screen)
    # vilain.voa()
#thingsfallin'
    soja.surja(screen)
    soja.cai()
#hitbox
    for bomba in objects1:
     bomba.surja(screen)
     bomba.cai()
     
    if playerI.mask.overlap(bomb.mask, (bomb.pos_x - playerI.pos_x,bomb.pos_y - playerI.pos_y)):
        print('u lost u r bad')
        running=False
    if playerI.mask.overlap(soja.mask, (soja.pos_x - playerI.pos_x,soja.pos_y - playerI.pos_y)):
        point+=1
        soja.pos_x=-9999
        soja.pos_y=90

    Score = texto.render(f"Pontuação: {point}", True,(0,0,255))
    screen.blit(Score,(0,10))
    if point >= 10:
        print('u won')
        break
    pygame.display.update()
    fps.tick(80)
    #paralax here

    #MAN I'M LOVING THAT SHIT WHAT

