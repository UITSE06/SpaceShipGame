#Khai bao thu vien
import Buttons
import SpaceShip2
import SoundManager
import Enemy
import ImageManager
import Player
import BackGround
import random, time, pygame, sys, copy, os
from pygame.locals import*

#Khoi tao ban dau
TEXTCOLOR = (239, 255, 255, 1)
SCREENHEIGHT = 600 #Chieu dai man hinh
SCREENWIDTH = 480 #Chieu ngang man hinh

class GameSpaceShip(object):
    class __GameSpaceShip():
        isGameOver = False
        screen = None
        gameImage = None
        gameplayerImage = None
        gameBulletImage = None
        textFont = None
        scoreImage = None
        lifeImage = None
        gameEnemyImage = None
        gameImageManager = None
        player = None
        backGround1 = None
        backGround2 = None
        sound = None
        score = 100
        listEnemy = []
        spawnEnemy = 0.05
        enemyTimeCurrent = 0
        btnRestart = None
        def __init__(self):
            pygame.init()
            self.gameImageManager = ImageManager.ImageManager()
            self.sound = SoundManager.SoundManager()
            self.player = Player.Player()
            self.backGround1 = BackGround.BackGround([0, -SCREENHEIGHT])
            self.backGround2 = BackGround.BackGround([0, 0])
            self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
            self.gameEnemyImage = self.gameImageManager.ENEMYIMAGE
            self.gameImage = self.gameImageManager.BGIMAGE
            self.gameBulletImage = self.gameImageManager.BULLETIMAGE
            self.gameImage = pygame.transform.smoothscale(self.gameImage, (SCREENWIDTH, SCREENHEIGHT))
            self.gameplayerImage = self.gameImageManager.PLAYERIMAGE
            self.gameplayerImage = pygame.transform.smoothscale(self.gameplayerImage, (self.player.playerSize[0], self.player.playerSize[1]))
            self.scoreImage = pygame.transform.smoothscale(self.gameImageManager.SCOREIMAGE, (35, 40))
            self.lifeImage =  pygame.transform.smoothscale(self.gameImageManager.LIFEIMAGE, (35, 40))
            self.gameBulletImage = pygame.transform.smoothscale(self.gameBulletImage, (10, 20))
            self.textFont = pygame.font.Font('GOUDYSTO.TTF', 25)
            self.btnRestart = Buttons.Button(self.gameImageManager.BUTTONRESTARTIMAGE)
            #sound.play()
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.7)
        def game_reset(self):
            self.isGameOver = False
            self.spawnEnemy = 0.05
            self.player.reset()
            if len(self.listEnemy) > 0:
                self.listEnemy.pop(len(self.listEnemy) - 1)
        def game_draw(self):
            self.screen.fill(0)
            self.screen.blit(self.gameplayerImage, (0, 0))
            self.screen.blit(self.gameImage, (self.backGround1.bgPos[0], self.backGround1.bgPos[1]))
            self.screen.blit(self.gameImage, (self.backGround2.bgPos[0], self.backGround2.bgPos[1]))
            self.draw_score()
            if self.isGameOver:
                self.draw_game_over()
            if not self.player.isDie:
                self.screen.blit(self.gameplayerImage, (self.player.playerPos[0], self.player.playerPos[1]))
            else:
                if self.player.playerLife > 0:
                    self.player.respawn()
            #screen.blit(gameBulletImage, (100, 100))
            listBullet = self.player.listBullet
            #print len(listBullet)
            for bulletItem in listBullet:
               #global gameBulletImage
               self.screen.blit(self.gameBulletImage, (bulletItem.bulletPos[0], bulletItem.bulletPos[1]))
            for enemyItem in self.listEnemy:
                enemyImage = None
                if enemyItem.enemyType == 'BASE':
                    enemyImage = self.gameEnemyImage[0]
                elif enemyItem.enemyType == 'TYPE1':
                    enemyImage = self.gameEnemyImage[1]
                else:
                    enemyImage = self.gameEnemyImage[2]
                enemyImage = pygame.transform.rotate(enemyImage, enemyItem.enemyAngle)
                self.screen.blit(enemyImage, (enemyItem.enemyPos[0], enemyItem.enemyPos[1]))
            pygame.display.flip()

        def draw_score(self):
            self.screen.blit(self.scoreImage, (20, 80))
            self.screen.blit(self.lifeImage, (20, 20))
            #life
            lifeImage = self.textFont.render(str(self.player.playerLife), 1, TEXTCOLOR)
            lifeRect = lifeImage.get_rect()
            lifeRect.bottomleft = (80, 65)
            self.screen.blit(lifeImage, lifeRect)
            #score
            scoreImage = self.textFont.render(str(self.score), 1, TEXTCOLOR)
            scoreRect = scoreImage.get_rect()
            scoreRect.bottomleft = (80, 115)
            self.screen.blit(scoreImage, scoreRect)
           
        def draw_game_over(self):
            gameOverImage = self.textFont.render('GAME OVER', 1, (255, 249, 153))
            gameOverRect = gameOverImage.get_rect()
            gameOverRect.bottomleft = (SCREENWIDTH /2 - gameOverRect.width / 2, SCREENHEIGHT / 2 - 50)
            self.screen.blit(gameOverImage, gameOverRect)
            self.btnRestart.create_button(self.screen, SCREENWIDTH / 2 - 110, SCREENHEIGHT / (2.5) + gameOverRect.height + 10, 220, 100)
        def spawn_enemy(self):
            #ENEMYTIMECURRENT += 0.0016
            types = list(range(len(Enemy.ENEMYTYPE)))
            typeIndex = random.choice(types)
            enemyObj = Enemy.Enemy()
            enemyObj.enemyPos[0] = random.randint(0, SCREENWIDTH - 50)
            enemyObj.enemyPos[1] = -10
            enemyObj.enemyType = Enemy.ENEMYTYPE[typeIndex]
            if enemyObj.enemyType == 'BASE':
               enemyObj.enemyMove = 5
            elif enemyObj.enemyType == 'TYPE1':
               enemyObj.enemyMove = 6
            else:
               enemyObj.enemyMove = 9
            self.listEnemy.append(enemyObj)   

        def game_input(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.player.move('M_LEFT')
            if key[pygame.K_RIGHT]:
                self.player.move('M_RIGHT')
            if key[pygame.K_UP]:
                self.player.move('M_UP')
            if key[pygame.K_DOWN]:
                self.player.move('M_DOWN')

        def game_update(self):
            self.backGround1.move(SCREENHEIGHT)
            self.backGround2.move(SCREENHEIGHT)
            self.player.shoot_spawn()
            self.player.collision(self.listEnemy)
            self.enemyTimeCurrent += 0.0016
            #print 'Time spawn_enemy %s' %ENEMYTIMECURRENT
            if self.score > 10000:
                self.score = 0
                if self.player.playerLife < 9:
                    self.player.playerLife += 1
                if self.spawnEnemy > 0.02:
                    self.spawnEnemy -= 0.005
            if self.player.playerLife == 0:
                if self.player.isDie == True:
                    self.isGameOver = True
            if not self.isGameOver == True:
                if self.enemyTimeCurrent > self.spawnEnemy:
                    self.spawn_enemy()
                    self.enemyTimeCurrent = 0
            for enemeObj in self.listEnemy:
                enemeObj.move()
                enemeObj.destroy()
                if enemeObj.isDestroy == True:
                    self.listEnemy.remove(enemeObj)
                    del enemeObj
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not GameSpaceShip.instance:
            GameSpaceShip.instance = GameSpaceShip.__GameSpaceShip()
        return GameSpaceShip.instance
