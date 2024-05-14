import pygame

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
# playerI=

fps = pygame.time.Clock()
running=True
while running:
    screen.blit(fundo, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.update()
    fps.tick(60)
    #paralax here
