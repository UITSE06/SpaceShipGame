#Khai bao thu vien
import SpaceShip
import random, time, pygame, sys, copy
from pygame.locals import*

ENEMYTYPE = ['BASE', 'TYPE1', 'TYPE']


class Enemy():
    enemyAngle = 0
    enemyType = 'BASE'
    enemyHP = 2
    enemySize = [0,0]
    enemyPos = [0,0]
    enemyMove = 5
    isDestroy = False
    def __init__(self, size, pos):
        self.enemySize = size
        self.enemyPos = pos
        self.rect = pygame.Rect(self.enemyPos[0], self.enemyPos[1], self.enemySize[0], self.enemySize[1])
    def __init__(self):
        self.enemySize = (45, 45)
        self.enemyPos = [0, 0]
        self.rect = pygame.Rect(self.enemyPos[0], self.enemyPos[1], self.enemySize[0], self.enemySize[1])
    def move(self):
        self.enemyPos[1] += self.enemyMove
        self.enemyAngle += 0.7
        self.rect = pygame.Rect(self.enemyPos[0], self.enemyPos[1], self.enemySize[0], self.enemySize[1])
    
    def destroy(self):
        if self.enemyPos[1] > SpaceShip.SCREENHEIGHT:
            self.isDestroy = True
    