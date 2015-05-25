import random, time, pygame, sys, copy
from pygame.locals import*

PLAYERPATH = 'ship.png'
BACKGROUNDPATH = 'bg_space1.png'
BULLETPATH = 'bullet.png'
ENEMYPATH = 'stone%s.png'
NUMENEMY = 3


class ImageManager(object):
    class __ImageManager:
        BGIMAGE = None
        PLAYERIMAGE = None
        BULLETIMAGE = None
        ENEMYIMAGE = []
        def __init__(self):
            self.BGIMAGE = pygame.image.load(BACKGROUNDPATH)
            self.PLAYERIMAGE = pygame.image.load(PLAYERPATH)
            self.BULLETIMAGE = pygame.image.load(BULLETPATH)
            for i in range(1, NUMENEMY + 1):
                imageItem = pygame.image.load(ENEMYPATH % i)
                imageItem = pygame.transform.smoothscale(imageItem, (50, 50))
                self.ENEMYIMAGE.append(imageItem)
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not ImageManager.instance:
            ImageManager.instance = ImageManager.__ImageManager()
        return ImageManager.instance