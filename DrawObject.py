import random, time, pygame, sys, copy
from pygame.locals import*

SCREENHEIGHT = 600 #Chieu dai man hinh
SCREENWIDTH = 480 #Chieu ngang man hinh

class DrawObject(object):
    class __DrawObject:
        def draw_object(img, pos, size):
            #Get object
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not DrawObject.instance:
            DrawObject.instance = DrawObject.__DrawObject()
        return DrawObject.instance