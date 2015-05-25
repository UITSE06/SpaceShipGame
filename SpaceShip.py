#Khai bao thu vien
import SoundManager
import Enemy
import ImageManager
import Player
import BackGround
import random, time, pygame, sys, copy, os
from pygame.locals import*

#Khoi tao ban dau
SCREENHEIGHT = 600 #Chieu dai man hinh
SCREENWIDTH = 480 #Chieu ngang man hinh
PLAYERSIZE = (70, 90)
SPAWNENEMY = 0.05
LISTENEMY = []
ENEMYTIMECURRENT = 0

def game_init():
    global SCREEN, GAMEBGIMAGE, GAMEPLAYERIMAGE, GAMEBULLETIMAGE, GAMEENEMYIMAGE , GAMEIMAGEMANAGER, PLAYER, BACKGROUND1, BACKGROUND2, CLOCK, SOUND
    pygame.init()
    GAMEIMAGEMANAGER = ImageManager.ImageManager()
    SOUND = SoundManager.SoundManager()
    PLAYER = Player.Player()
    BACKGROUND1 = BackGround.BackGround([0, -SCREENHEIGHT])
    BACKGROUND2 = BackGround.BackGround([0, 0])
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GAMEENEMYIMAGE = GAMEIMAGEMANAGER.ENEMYIMAGE
    GAMEBGIMAGE = GAMEIMAGEMANAGER.BGIMAGE
    GAMEBULLETIMAGE = GAMEIMAGEMANAGER.BULLETIMAGE
    #GAMEBULLETIMAGE = pygame.transform.smoothscale(GAMEBULLETIMAGE, (10, 20))
    GAMEBGIMAGE = pygame.transform.smoothscale(GAMEBGIMAGE, (SCREENWIDTH, SCREENHEIGHT))
    GAMEPLAYERIMAGE = GAMEIMAGEMANAGER.PLAYERIMAGE
    GAMEPLAYERIMAGE = pygame.transform.smoothscale(GAMEPLAYERIMAGE, (PLAYER.playerSize[0], PLAYER.playerSize[1]))
    CLOCK = pygame.time.Clock()
    #SOUND.play()
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.7)

def game_draw():
    SCREEN.fill(0)
    SCREEN.blit(GAMEBGIMAGE, (BACKGROUND1.bgPos[0], BACKGROUND1.bgPos[1]))
    SCREEN.blit(GAMEBGIMAGE, (BACKGROUND2.bgPos[0], BACKGROUND2.bgPos[1]))
    if not PLAYER.isDie:
        SCREEN.blit(GAMEPLAYERIMAGE, (PLAYER.playerPos[0], PLAYER.playerPos[1]))
    else:
        if PLAYER.playerLife > 0:
            PLAYER.respawn()
    #SCREEN.blit(GAMEBULLETIMAGE, (100, 100))
    listBullet = PLAYER.listBullet
    #print len(listBullet)
    for bulletItem in listBullet:
       global GAMEBULLETIMAGE
       GAMEBULLETIMAGE = pygame.transform.smoothscale(GAMEBULLETIMAGE, (bulletItem.bulletSize[0], bulletItem.bulletSize[1]))
       SCREEN.blit(GAMEBULLETIMAGE, (bulletItem.bulletPos[0], bulletItem.bulletPos[1]))
    for enemyItem in LISTENEMY:
        enemyImage = None
        if enemyItem.enemyType == 'BASE':
            enemyImage = GAMEENEMYIMAGE[0]
        elif enemyItem.enemyType == 'TYPE1':
            enemyImage = GAMEENEMYIMAGE[1]
        else:
            enemyImage = GAMEENEMYIMAGE[2]
        enemyImage = pygame.transform.rotate(enemyImage, enemyItem.enemyAngle)
        SCREEN.blit(enemyImage, (enemyItem.enemyPos[0], enemyItem.enemyPos[1]))
    pygame.display.flip()

def spawn_enemy():
    #ENEMYTIMECURRENT += 0.0016
    types = list(range(len(Enemy.ENEMYTYPE)))
    typeIndex = random.choice(types)
    enemyObj = Enemy.Enemy()
    enemyObj.enemyPos[0] = random.randint(0, SCREENWIDTH - 50)
    enemyObj.enemyPos[1] = -10
    enemyObj.enemyType = Enemy.ENEMYTYPE[typeIndex]
    LISTENEMY.append(enemyObj)   

def game_input():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        PLAYER.move('M_LEFT')
    if key[pygame.K_RIGHT]:
        PLAYER.move('M_RIGHT')
    if key[pygame.K_UP]:
        PLAYER.move('M_UP')
    if key[pygame.K_DOWN]:
        PLAYER.move('M_DOWN')

def game_update():
    BACKGROUND1.move(SCREENHEIGHT)
    BACKGROUND2.move(SCREENHEIGHT)
    PLAYER.shoot_spawn()
    PLAYER.collision(LISTENEMY)
    global ENEMYTIMECURRENT
    ENEMYTIMECURRENT += 0.0016
    print 'Time spawn_enemy %s' %ENEMYTIMECURRENT
    if ENEMYTIMECURRENT > SPAWNENEMY:
        spawn_enemy()
        ENEMYTIMECURRENT = 0
    for enemeObj in LISTENEMY:
        enemeObj.move()
        enemeObj.destroy()
        if enemeObj.isDestroy == True:
            LISTENEMY.remove(enemeObj)
            del enemeObj

def main():
    game_init()
    while True: 
        game_update()
        game_input()
        game_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        CLOCK.tick(60)

if __name__ == '__main__':
    main()