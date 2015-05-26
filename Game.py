#Khai bao thu vien
import SpaceShip2
import random, time, pygame, sys, copy, math
from pygame.locals import*

def main():
    global CLOCK
    CLOCK = None
    CLOCK = pygame.time.Clock()
    game = SpaceShip2.GameSpaceShip()
    #game.game_init()
    while True: 
        game.game_update()
        game.game_input()
        game.game_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                CLOCK.tick(FPS)

if __name__ == '__main__':
    main()