import pygame, sys, time, random, math
from pygame.locals import *
SHOE=pygame.image.load('shoe.png')
class user(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.x=x
        self.y=y-22
        self.image=SHOE
        self.rotation=0
        self.rect=pygame.Rect(self.x,self.y,18,10)
    def attatch(self,x,y):
        self.rect.x=x+self.rotation
        self.rect.y=y+self.rotation
    def rotation(self,x,y):
        -abs(sqrt(y))=x+25