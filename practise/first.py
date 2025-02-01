#first game window
import pygame as pg
import random
import math
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

bullet_speed=0.8
#GAME LOOP
score=0

# player   
def player(x,y):
    screen.blit(player_img,(x,y))
#enemy
def ufo(x,y):
    screen.blit(ufo_img,(x,y))    
def bullet(x,y): 
    screen.blit(bullet_img,(x,y))     
    
def is_collision(ufo_x, ufo_y, bullet_x, bullet_y):
    distance = math.sqrt((ufo_x - bullet_x) ** 2 + (ufo_y - bullet_y) ** 2)
    return distance < 27  # Collision threshold     

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
        bullet_x=playerx+24    
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
        
    if is_collision(ufox, ufoy, bullet_x, bullet_y):
        print("💥 Enemy Hit! 💥")  # Print message in console (Replace with score system later)
        bullet_y = playery  # Reset bullet
        bullet_state = "ready"
        ufox = random.randint(50, 750)  # Move enemy to a new random position
        ufoy = random.randint(50, 150)  
        score +=1
        
    if ufoy >= 400:
        print("Game Over!")
        font = pg.font.Font(None, 64)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (250, 250))
        pg.display.update()
        pg.time.delay(2000)  # Pause for 2 seconds before closing
        running = False
 
                  
        
                             
    
    player(playerx,playery)
    ufo(ufox,ufoy)
    pg.display.update()