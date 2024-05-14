import pygame


class things:
    def __init__(self,arquivoimagem,largura,altura,x,y):
        self.imagem = pygame.image.load(arquivoimagem)

        self.largura = largura
        self.altura = altura

        self.pos_x=x
        self.pos_y=y
        self.speed=8
    def cai(self):
        self.pos_y += self.speed
        if self.pos_y>=650:
            self.pos_y=0
    def surja(self,tela):
        tela.blit(self.imagem, (self.pos_x,self.pos_y))