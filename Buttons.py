# -*- coding: cp1252 -*-
#/usr/bin/env python
#Simon H. Larsen
#Buttons
#Project startet: d. 26. august 2012
import pygame
from pygame.locals import *
pygame.init()
class Button:
    image = None
    isPress = False
    alpha = 255

    def __init__(self):
        self.image = None

    def __init__(self, image):
        self.image = image
   

    def create_button(self, surface, x, y, width, height):
        surface = self.draw_button(surface, width, height, x, y)
        self.rect = pygame.Rect(x,y, width, height)
        return surface

    def draw_button(self, surface, width, height, x, y):    
        self.image = pygame.transform.smoothscale(self.image, (width,height))
        #self.image = pygame.transform.smoothscale(self.image, (length,height))
        #surface.blit(self.image, (x,y)) 
        self.blit_alpha(surface, self.image, (x,y), self.alpha)
        return surface

    def blit_alpha(self, target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

    def update_button(self, event):
        if event.type == MOUSEBUTTONDOWN:
           self.pressed(pygame.mouse.get_pos())
        elif event.type == MOUSEMOTION:
           self.hovered(pygame.mouse.get_pos())
        elif event.type == MOUSEBUTTONUP:
           self.un_pressed()

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        self.alpha = 200
                        self.isPress = True

    def un_pressed(self):
        self.alpha = 255
        self.isPress = False

    def hovered(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        self.alpha = 230
                        return True
                    else: 
                        self.alpha = 255
                        return False
                else: 
                    self.alpha = 255
                    return False
            else:
                 self.alpha = 255
                 return False
        else:
            self.alpha = 255
            return False

