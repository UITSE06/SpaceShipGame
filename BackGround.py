#Khai bao thu vien
import random, time, pygame, sys, copy
from pygame.locals import*

class BackGround():

    bgSize = [0,0]
    bgPos = [0,0]
    bgMove = 2
    def __init__(self, size, pos):
        self.bgSize = size
        self.bgPos = pos
    def __init__(self):
        self.bgSize = (480, 600)
        self.bgPos = [0, 0]
    def __init__(self, pos):
        self.bgSize = (480, 600)
        self.bgPos = pos
    def move(self, screenHeight):
        self.bgPos[1] += self.bgMove
        if self.bgPos[1] >= screenHeight:
           self.bgPos[1] = -screenHeight