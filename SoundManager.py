import SoundManager
import random, time, pygame, sys, copy
from pygame.locals import*

BGSOUNDPATH = 'music_background.wav'
BULLETSOUNDPATH = 'weapon_player.wav'
BULLETDESTROYPATH = 'explosion_asteroid.wav'
PLAYERDESTROYPATH = 'explosion_player.wav'
ENEMYDESTROYPATH = 'explosion_enemy.wav'
#ENEMYSOUNDPATH = 'stone%s.png'
NUMENEMY = 3

class SoundManager(object):
    class __SoundManager:
        BGSOUND = None
        BULLETSOUND = None
        PLAYERDESTROYSOUND = None
        BULLETDESTROYSOUND = None
        ENEMYDESTROYSOUND = None
        ENEMYSOUND = []
        def __init__(self):
            self.BGSOUND = pygame.mixer.music.load(BGSOUNDPATH)
            self.BULLETSOUND = pygame.mixer.Sound(BULLETSOUNDPATH)
            self.PLAYERDESTROYSOUND = pygame.mixer.Sound(PLAYERDESTROYPATH)
            self.ENEMYDESTROYSOUND = pygame.mixer.Sound(ENEMYDESTROYPATH)
            self.BULLETDESTROYSOUND = pygame.mixer.Sound(BULLETDESTROYPATH)
            #for i in range(1, NUMENEMY + 1):
              #  soundItem = pygame.mixer.Sound(ENEMYSOUNDPATH % i)
                #self.ENEMYSOUND.append(soundItem)
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not SoundManager.instance:
            SoundManager.instance = SoundManager.__SoundManager()
        return SoundManager.instance