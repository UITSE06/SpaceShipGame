import random, time, pygame, sys, copy
from pygame.locals import*

LIFEPATH = 'life.png'
SCOREPATH = 'score.png'
PLAYERPATH = 'ship.png'
BACKGROUNDPATH = 'bg_space1.png'
BULLETPATH = 'bullet.png'
ENEMYPATH = 'stone%s.png'
BUTTONSTARTPATH = 'bt_start.png'
BUTTONOPTIONPATH = 'bt_option.png'
BUTTONSCOREPATH = 'bt_score.png'
BUTTONRESTARTPATH = 'bt_restart.png'
BUTTONSAVEPATH = 'bt_save.png'
INPUTPATH = 'input_score.png'
MENUPATH = 'bg_menu1.png'
SAVESCOREPATH = 'bg_saveScore1.png'
NUMENEMY = 3


class ImageManager(object):
    class __ImageManager:
        def __init__(self):
            self.ENEMYIMAGE = []
            self.BGIMAGE = pygame.image.load(BACKGROUNDPATH)
            self.PLAYERIMAGE = pygame.image.load(PLAYERPATH)
            self.BULLETIMAGE = pygame.image.load(BULLETPATH)
            self.SCOREIMAGE = pygame.image.load(SCOREPATH)
            self.LIFEIMAGE = pygame.image.load(LIFEPATH)
            self.BUTTONOPTIONIMAGE = pygame.image.load(BUTTONOPTIONPATH)
            self.BUTTONSTARTIMAGE = pygame.image.load(BUTTONSTARTPATH)
            self.BUTTONRESTARTIMAGE = pygame.image.load(BUTTONRESTARTPATH)
            self.BUTTONSCOREIMAGE = pygame.image.load(BUTTONSCOREPATH)
            self.BUTTONSAVEIMAGE = pygame.image.load(BUTTONSAVEPATH)
            self.INPUTIMAGE = pygame.image.load(INPUTPATH)
            self.MENUIMAGE = pygame.image.load(MENUPATH)
            self.SAVESCOREIMAGE = pygame.image.load(SAVESCOREPATH)
            for i in range(1, NUMENEMY + 1):
                imageItem = pygame.image.load(ENEMYPATH % i)
                imageItem = pygame.transform.smoothscale(imageItem, (50, 50))
                self.ENEMYIMAGE.append(imageItem)
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not ImageManager.instance:
            ImageManager.instance = ImageManager.__ImageManager()
        return ImageManager.instance