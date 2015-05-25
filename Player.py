#Khai bao thu vien
import SpaceShip
import Bullet
import random, time, pygame, sys, copy, decimal
from pygame.locals import*

PLAYERPATH = 'ship.png'
class Player():
    playerLife = 5
    isDie = False
    playerSize = [0,0]
    playerPos = [0,0]
    playerMove = 5
    listBullet = []
    timeCurrent = 0
    timeShoot = 0.3
    timeDieCurrent = 0
    timeRespawn = 0.8
    def __init__(self, size, pos):
        self.playerSize = size
        self.playerPos = pos
        self.rect = pygame.Rect(self.playerPos[0], self.playerPos[1], self.playerSize[0], self.playerSize[1])
    def __init__(self):
        self.playerSize = (60, 70)
        self.playerPos = [SpaceShip.SCREENWIDTH / 2, SpaceShip.SCREENHEIGHT - self.playerSize[1]]
        self.rect = pygame.Rect(self.playerPos[0], self.playerPos[1], self.playerSize[0], self.playerSize[1])
    def move(self, moveType):
        self.move_single_axis(moveType)
        if self.playerPos[1] > SpaceShip.SCREENHEIGHT - self.playerSize[1]:
            self.playerPos[1] =  SpaceShip.SCREENHEIGHT - self.playerSize[1]
        elif self.playerPos[1] < 0:
            self.playerPos[1] = 0
        elif self.playerPos[0] > SpaceShip.SCREENWIDTH - self.playerSize[0]:
            self.playerPos[0] =  SpaceShip.SCREENWIDTH - self.playerSize[0]
        elif self.playerPos[0] < 0:
            self.playerPos[0] = 0
        self.rect = pygame.Rect(self.playerPos[0], self.playerPos[1], self.playerSize[0], self.playerSize[1])

    def shoot(self):
        bullet = None 
        self.timeCurrent += 0.016
        if self.timeCurrent >= self.timeShoot:
            self.timeCurrent = 0
            bullet = Bullet.Bullet()
            bullet.bulletPos[0] = self.playerPos[0] + self.playerSize[0] / 2 - 5
            bullet.bulletPos[1] = self.playerPos[1] - self.playerSize[1] / 2
            self.listBullet.append(bullet)

    def shoot_spawn(self):
        if not self.isDie:
            self.shoot()
        for bulletItem in self.listBullet:
            bulletItem.move()
            bulletItem.destroy()
            if bulletItem.isDestroy == True:
                self.listBullet.remove(bulletItem)
                del bulletItem

    def collision(self, ListEnemy):
        for bulletItem in self.listBullet:
            bulletItem.collision(ListEnemy)
        if not self.isDie:
            for enemyObj in ListEnemy:
                if self.rect.colliderect(enemyObj.rect):
                    enemyObj.isDestroy = True
                    self.isDie = True

    def respawn(self):
        self.timeDieCurrent += 0.016
        if self.timeDieCurrent >= self.timeRespawn:
            self.timeDieCurrent = 0
            self.isDie = False
            self.playerLife -= 1;

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