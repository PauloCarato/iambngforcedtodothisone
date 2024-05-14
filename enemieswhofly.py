import pygame

class enemy:
    def __init__(self,arquivoimagem,largura,altura,x,y):
        self.imagem = pygame.image.load(arquivoimagem)

        self.largura = largura
        self.altura = altura

        self.pos_x=x
        self.pos_y=y

    def surja(self,tela):
        tela.blit(self.imagem, (self.pos_x,self.pos_y))