# -*- coding: cp1252 -*-
#/usr/bin/env python
#Simon H. Larsen
#inputs
#Project startet: d. 26. august 2012
import pygame
from pygame.locals import *
pygame.init()
class Input:
    image = None
    isPress = False
    alpha = 255

    def __init__(self):
        self.image = None

    def __init__(self, image, color, maxLen):
        self.image = image
        self.text = []
        self.color = color
        self.rect = None
        self.maxLen = maxLen
        self.textFont = pygame.font.Font('GOUDYSTO.TTF', 25)
   

    def create_input(self, surface, x, y, width, height):
        self.rect = pygame.Rect(x,y, width, height)
        surface = self.draw_input(surface, width, height, x, y)
        return surface

    def draw_input(self, surface, width, height, x, y):    
        self.image = pygame.transform.smoothscale(self.image, (width,height))
        surface.blit(self.image, (x,y)) 
        textPrint = ''.join(self.text)
        textImage = self.textFont.render(textPrint, 1, self.color)
        textRect = textImage.get_rect()
        textRect.bottomleft = (x + 10, y + height)
        surface.blit(textImage, textRect)
        #self.blit_alpha(surface, self.image, (x,y), self.alpha)
        return surface

    def blit_alpha(self, target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

    def update_input(self, event):
        if event.type == KEYDOWN:
            if event.key == 8:
               self.text_change(None)
            elif event.key >= 65 and event.key <=122:
               self.text_change(chr(event.key))

    def text_change(self, temp):
       if not temp == None:   
           if len(self.text) < self.maxLen:
              self.text.append(temp)
       else:
           if len(self.text) > 0:
              del self.text[len(self.text) - 1]


