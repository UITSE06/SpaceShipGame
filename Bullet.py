#Khai bao thu vien
import SpaceShip2
import SoundManager
import random, time, pygame, sys, copy, math
from pygame.locals import*

class Bullet():
    bulletAngle = 0
    bulletSize = [0,0]
    bulletPos = [0,0]
    bulletMove = 5
    isDestroy = False
    def __init__(self, size, pos):
        self.bulletSize = size
        self.bulletPos = pos
        self.rect = pygame.Rect(self.bulletPos[0], self.bulletPos[1], self.bulletSize[0], self.bulletSize[1])
    def __init__(self):
        self.bulletSize = (10, 20)
        self.bulletPos = [0, 0]
        self.bulletAngle = 0
        self.rect = pygame.Rect(self.bulletPos[0], self.bulletPos[1], self.bulletSize[0], self.bulletSize[1])
    def move(self):
        self.bulletPos[1] -= self.bulletMove
        #self.bulletPos[0] -= self.bulletMove * math.sin(-math.pi / 4)
        self.rect = pygame.Rect(self.bulletPos[0], self.bulletPos[1], self.bulletSize[0], self.bulletSize[1])
    
    def collision(self, ListEnemy): 
        for enemyObj in ListEnemy:
            if self.rect.colliderect(enemyObj.rect):
                self.isDestroy = True
                enemyObj.isDestroy = True
                SpaceShip2.GameSpaceShip().score += 100
                SoundManager.SoundManager().ENEMYDESTROYSOUND.play()
                break

    def destroy(self):
        if self.bulletPos[1] < 0:
            self.isDestroy = True
    