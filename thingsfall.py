import pygame
import random
from thiswillmakemyworkeasier import *


class fall:
    def __init__(self,arquivoimagem,largura,altura):
        self.imagem = pygame.image.load(arquivoimagem)

        self.largura = largura
        self.altura = altura

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x=random.randint(0,1200)
        self.pos_y=0
        self.speed=random.randint(0,15)
        self.mask = pygame.mask.from_surface(self.imagem)
    def cai(self):
        self.pos_y += self.speed
        if self.pos_y>=650:
            self.pos_y=0
            self.pos_x=random.randint(0,1200)
            self.speed=random.randint(5,10)
    def surja(self,tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))