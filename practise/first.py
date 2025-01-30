#first game window
import pygame as pg
import random
pg.init()#initialize the screen
screen=pg.display.set_mode((800,600))#inside it is a tuple so two small braces
running=True

pg.display.set_caption("Space-Invader")
#icon=pg.image.load("practise/ufo.png")
#pg.display.set_icon(icon )
#player
player_img=pg.image.load("practise/spaceship.png")
playerx=400
playery=530
#enemy ufo
ufo_img=pg.image.load("practise/ufo.png")
ufox=40
ufoy=40
ufospeed=0.3
space_img=pg.image.load("practise/space.jpg")
#bullet
bullet_img=pg.image.load("practise/bullet.png")

bullet_speed=0.3
#GAME LOOP


# player   
def player(x,y):
    screen.blit(player_img,(x,y))
#enemy
def ufo(x,y):
    screen.blit(ufo_img,(x,y))    
def bullet(x,y): 
    screen.blit(bullet_img,(x,y))      

bullet_x=playerx+24
bullet_y=playery-15     
while running:
    screen.fill((0,0,0))
    screen.blit(space_img,(0,0))
    
    keys = pg.key.get_pressed()  
    for event in pg.event.get():
        
        if event.type ==pg.QUIT:
             running=False
    ufox += ufospeed
     # Reverse at edges
    if ufox >= 750 or ufox <= 0:
        ufoy +=30
        ufospeed *= -1 
      
  
    if bullet_y>0:
        bullet_y -=bullet_speed
    elif bullet_y<=0:
        bullet_y=playery-15
        bullet_x=playerx=24    
    bullet(bullet_x,bullet_y)      
  
    
         
       
    if event.type==pg.KEYDOWN:
        if event.key==pg.K_LEFT:
            playerx-=0.1
        if event.key==pg.K_RIGHT:
                playerx+=0.1
    if event.type==pg.KEYUP:
        if event.key==pg.K_LEFT or event.key==pg.K_RIGHT:
                    playerx+=0   
    if (playerx<=0):
        playerx=0
    if (playerx>=730):
        playerx=730                 
        
                             
    
    player(playerx,playery)
    ufo(ufox,ufoy)
    pg.display.update()