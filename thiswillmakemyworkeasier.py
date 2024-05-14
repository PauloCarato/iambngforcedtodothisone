import pygame

class playercls:
    def __init__(self,arquivoimagem,largura,altura,x,y):
        self.imagem = pygame.image.load(arquivoimagem)

        self.largura = largura
        self.altura = altura

        self.pos_x=x
        self.pos_y=y
        self.mask = pygame.mask.from_surface(self.imagem) 

    def surja(self,tela):
        tela.blit(self.imagem, (self.pos_x,self.pos_y))

    def move(self,right,left):
        moving=pygame.key.get_pressed()
        if moving[right]:
            self.pos_x += 7
        if moving[left]:
            self.pos_x -= 7.25