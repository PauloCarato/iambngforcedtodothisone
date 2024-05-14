import pygame

class enemy:
    def __init__(self,arquivoimagem,largura,altura,x,y):
        self.imagem = pygame.image.load(arquivoimagem)

        self.largura = largura
        self.altura = altura

        self.pos_x=x
        self.pos_y=y
        self.speed=8
        self.mask = pygame.mask.from_surface(self.imagem) #this specific line wasnt code by me (sorry i'm lazy)

    def surja(self,tela):
        tela.blit(self.imagem, (self.pos_x,self.pos_y))
    def voa(self):
        self.pos_x += self.speed
        if self.pos_x>=1200:
            self.pos_x=-300

#hope it works