#Khai bao thu vien
import Menu
import SpaceShip2
import random, time, pygame, sys, copy, math
from pygame.locals import*

def main():
    global CLOCK
    CLOCK = None
    CLOCK = pygame.time.Clock()
    #game = SpaceShip2.GameSpaceShip()
    menu = Menu.GameMenu()
    #game.game_init()
    while True: 
        #game.game_update()
        #game.game_input()
        #game.game_draw()
        menu.game_update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                CLOCK.tick(FPS)
            else:
                menu.game_input(event)

if __name__ == '__main__':
    main()