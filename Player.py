#Khai bao thu vien
import Bullet
import random, time, pygame, sys, copy, decimal
from pygame.locals import*

PLAYERPATH = 'ship.png'
class Player():
    playerSize = [0,0]
    playerPos = [0,0]
    playerMove = 5
    listBullet = []
    timeCurrent = 0
    timeShoot = 0.3
    def __init__(self, size, pos):
        self.playerSize = size
        self.playerPos = pos
        self.rect = pygame.Rect(self.playerPos[0], self.playerPos[1], self.playerSize[0], self.playerSize[1])
    def __init__(self):
        self.playerSize = (70, 90)
        self.playerPos = [0, 0]
        self.rect = pygame.Rect(self.playerPos[0], self.playerPos[1], self.playerSize[0], self.playerSize[1])
    def move(self, moveType):
        self.move_single_axis(moveType)
    
    def shoot(self):
        bullet = None 
        self.timeCurrent += 0.016
        if self.timeCurrent >= self.timeShoot:
            self.timeCurrent = 0
            bullet = Bullet.Bullet()
            bullet.bulletPos[0] = self.playerPos[0] + self.playerSize[0] / 2
            bullet.bulletPos[1] = self.playerPos[1] - self.playerSize[1] / 2
            self.listBullet.append(bullet)
        for bulletItem in self.listBullet:
            bulletItem.move()
            bulletItem.destroy()
            if bulletItem.isDestroy == True:
                self.listBullet.remove(bulletItem)
                del bulletItem
    def shoot_spawn(self):
        self.shoot()

    def move_single_axis(self, moveType):
        
        # Move the rect
        if moveType == 'M_LEFT':
            self.rect.x -= self.playerMove
            self.playerPos[0] -= self.playerMove
        elif moveType == 'M_RIGHT':
            self.rect.x += self.playerMove
            self.playerPos[0] += self.playerMove
        elif moveType == 'M_UP':
            self.rect.y -= self.playerMove
            self.playerPos[1] -= self.playerMove
        else:
            self.rect.y += self.playerMove
            self.playerPos[1] += self.playerMove