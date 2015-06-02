#Khai bao thu vien
import Buttons
import SpaceShip2
import ImageManager
import Inputs;
import random, time, pygame, sys, copy, os
from pygame.locals import*

#Khoi tao ban dau
TEXTCOLOR = (239, 255, 255, 1)
SCREENHEIGHT = 600 #Chieu dai man hinh
SCREENWIDTH = 480 #Chieu ngang man hinh

class GameSaveScore(object):
    class __GameSaveScore():
        gameImageManager = None
        gameScreen = None
        backGround = None
        foreGround = None
        def __init__(self):
            pygame.init()
            self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
            self.gameImageManager = ImageManager.ImageManager()
            self.backGround = self.gameImageManager.MENUIMAGE
            self.foreGround = self.gameImageManager.SAVESCOREIMAGE
            self.btnSave = Buttons.Button(self.gameImageManager.BUTTONSAVEIMAGE)
            self.foreGround = pygame.transform.smoothscale(self.foreGround, (SCREENWIDTH, SCREENHEIGHT))
            self.backGround = pygame.transform.smoothscale(self.backGround, (SCREENWIDTH, SCREENHEIGHT))
            self.inputText = Inputs.Input(self.gameImageManager.INPUTIMAGE, (255,255,255), 10)

        def game_draw(self):
            self.screen.fill(0)
            self.screen.blit(self.backGround, (0,0))
            self.screen.blit(self.foreGround, (0,0))
            self.inputText.create_input(self.screen, 50,50, 300, 50)
            self.btnSave.create_button(self.screen, SCREENWIDTH / 2 - 100, SCREENHEIGHT / (2.5) + 200, 100, 100)
            pygame.display.flip()

        def game_input(self, event):
            self.inputText.update_input(event)
            self.btnSave.update_button(event)

        def game_update(self):
           print ''
                
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not GameSaveScore.instance:
            GameSaveScore.instance = GameSaveScore.__GameSaveScore()
        return GameSaveScore.instance

def main():
     while True: 
        #GameSaveScore().game_update()
        GameSaveScore().game_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            else:
                GameSaveScore().game_input(event)

if __name__ == '__main__':
    main()