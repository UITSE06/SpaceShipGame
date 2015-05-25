import random, time, pygame, sys, copy
from pygame.locals import*

PLAYERPATH = 'ship.png'
BACKGROUNDPATH = 'bg_space1.png'
ENEMYPATH = 'gem%s.png'
NUMENEMY = 3


class TypeObject(object):
    class __TypeObject:
        BGIMAGE = None
        PLAYERIMAGE = None
        ENEMYIMAGE = []
        def __init__(self):
            self.BGIMAGE = pygame.image.load(BACKGROUNDPATH)
            self.PLAYERIMAGE = pygame.image.load(PLAYERPATH)
            for i in range(1, NUMENEMY + 1):
                imageItem = pygame.image.load(ENEMYPATH % i)
                ENEMYIMAGE.append(imageItem)
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not TypeObject.instance:
            TypeObject.instance = TypeObject.__TypeObject()
        return TypeObject.instance