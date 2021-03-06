import pygame

import random



pygame.init()



screen = pygame.display.set_mode((800,600))



background = pygame.image.load('spacebackground.png')







#title and icon

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load('space-ship.png')

pygame.display.set_icon(icon)



#Player



playerImg = pygame.image.load('ship2.png')

playerX = 60

playerY = 500

playerX_change = 0

playerY_change = 0



#enemy



enemyImg = pygame.image.load('alien.png')

enemyX = random.randint(64,736)

enemyY = random.randint(64,150)

enemyX_change = 3

enemyY_change = 40



#bullet



#Ready - You can't see the bullet on the screen

#Fire - The bullet is currently moving



bulletImg = pygame.image.load('bullet.png')

bulletX = 0

bulletY = 500

bulletX_change = 0

bulletY_change = 10

bullet_state = "ready"





def player(x,y):

    screen.blit(playerImg,(x,y))



def enemy(x,y):

    screen.blit(enemyImg,(x,y))



def fire_bullet(x,y):

    global bullet_state

    bullet_state = "fire"

    screen.blit(bulletImg,(x+16,y+10))

    



running = True

while running:



  screen.fill((0,0,0))

  #background Image

  screen.blit(background,(0,0))

  



    

  for event in pygame.event.get():

    if event.type== pygame.QUIT:

      running = False

  

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT:

            playerX_change = -9.9



        if event.key == pygame.K_RIGHT:

            playerX_change = 9.9



        if event.key ==pygame.K_SPACE:

            if bullet_state is "ready":



                bulletX = playerX

                fire_bullet(bulletX,bulletY)





    if event.type == pygame.KEYUP:

        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

            playerX_change = 0



   #check for boundaries of spaceship so it doesn't go out of bounds 



  playerX += playerX_change



  if playerX <0:

      playerX = 0

  elif playerX >=736:

      playerX = 736



  enemyX += enemyX_change



  if enemyX <0:

      enemyX_change = 3

      enemyY +=enemyY_change

  elif enemyX >=736:

      enemyX_change = -3

      enemyY +=enemyY_change



    #bullet movement



  if bulletY <= 0:

      bulletY = 480

      bullet_state = "ready"



  if bullet_state is "fire":

     

      fire_bullet(bulletX,bulletY)

      bulletY -=bulletY_change

        

  player(playerX,playerY)

  enemy(enemyX,enemyY)



  pygame.display.update()