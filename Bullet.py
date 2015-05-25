#Khai bao thu vien
import random, time, pygame, sys, copy
from pygame.locals import*

class Bullet():

    bulletSize = [0,0]
    bulletPos = [0,0]
    bulletMove = 5
    isDestroy = False
    def __init__(self, size, pos):
        self.bulletSize = size
        self.bulletPos = pos
        self.rect = pygame.Rect(self.bulletPos[0], self.bulletPos[1], self.bulletSize[0], self.bulletSize[1])
    def __init__(self):
        self.bulletSize = (34, 34)
        self.bulletPos = [0, 0]
        self.rect = pygame.Rect(self.bulletPos[0], self.bulletPos[1], self.bulletSize[0], self.bulletSize[1])
    def move(self):
        self.bulletPos[1] -= self.bulletMove
    
    def destroy(self):
        if self.bulletPos[1] < 0:
            self.isDestroy = True
    