#Khai bao thu vien
import SpaceShip2
import ImageManager
import Buttons;
import random, time, pygame, sys, copy, os
from pygame.locals import*

#Khoi tao ban dau
TEXTCOLOR = (239, 255, 255, 1)
SCREENHEIGHT = 600 #Chieu dai man hinh
SCREENWIDTH = 480 #Chieu ngang man hinh

class GameMenu(object):
    class __GameMenu():
        game = SpaceShip2.GameSpaceShip()
        gameImageManager = None
        gameScreen = None
        btnOption = None
        btnStart = None
        btnScore = None
        backGround = None
        isRunGame = False
        def __init__(self):
            pygame.init()
            self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
            self.gameImageManager = ImageManager.ImageManager()
            self.btnStart = Buttons.Button(self.gameImageManager.BUTTONSTARTIMAGE)
            self.btnOption = Buttons.Button(self.gameImageManager.BUTTONOPTIONIMAGE)
            self.btnScore = Buttons.Button(self.gameImageManager.BUTTONSCOREIMAGE)
            self.backGround = self.gameImageManager.MENUIMAGE
            self.backGround = pygame.transform.smoothscale(self.backGround, (SCREENWIDTH, SCREENHEIGHT))
            self.textFont = pygame.font.Font('GOUDYSTO.TTF', 25)

        def game_draw(self):
            self.screen.fill(0)
            self.screen.blit(self.backGround, (0,0))
            self.btnStart.create_button(self.screen, SCREENWIDTH / 2 - 100, SCREENHEIGHT / (2.5), 200, 100)
            self.btnScore.create_button(self.screen, SCREENWIDTH / 2 - 100, SCREENHEIGHT / (2.5)+ 100, 200, 100)
            self.btnOption.create_button(self.screen, SCREENWIDTH / 2 - 100, SCREENHEIGHT / (2.5) + 200, 200, 100)
            pygame.display.flip()

        def game_input(self, event):
            if not self.isRunGame == True: 
                self.btnStart.update_button(event)
                self.btnOption.update_button(event)
                self.btnScore.update_button(event)
            elif self.game.isGameOver == True:
                self.game.btnRestart.update_button(event)

        def game_update(self):
            if self.btnStart.isPress == True:
                self.game.game_reset()
                self.isRunGame = True
                self.btnStart.isPress = False
            if self.game.btnRestart.isPress == True:
                self.isRunGame = False
                self.game.btnRestart.isPress = False
            if self.isRunGame == True:
                self.game.game_update()
                self.game.game_input()
                self.game.game_draw()
            else:
                self.game_draw()
                
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not GameMenu.instance:
            GameMenu.instance = GameMenu.__GameMenu()
        return GameMenu.instance

#def main():
  #   while True: 
     #   GameMenu().game_update()
        #GameMenu.game_draw()
     #   for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
          #      pygame.quit()
        #        exit(0)
         #   else:
          #      GameMenu().game_input(event)

#if __name__ == '__main__':
#    main()