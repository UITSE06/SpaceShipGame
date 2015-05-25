import random, time, pygame, sys, copy
from pygame.locals import*

PLAYERPATH = 'ship.png'
BACKGROUNDPATH = 'bg_space1.png'

class OnlyOne(object):
    class __OnlyOne:
        bgImage = None
        playerImage = None
        def __init__(self):
            self.bgImage = pygame.image.load(BACKGROUNDPATH)
            self.playerImage = pygame.image.load(PLAYERPATH)
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance
