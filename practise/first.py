#first game window
import pygame as pg
pg.init()#initialize the screen
screen=pg.display.set_mode((800,600))#inside it is a tuple so two small braces
running=True

pg.display.set_caption("Space-Invader")
icon=pg.image.load("practise/ufo.png")
pg.display.set_icon(icon )
player_img=pg.image.load("practise/spaceship.png")
playerx=400
playery=530
#GAME LOOP
def player():
    screen.blit(player_img,(playerx,playery))
while running:
    for event in pg.event.get():
        if event.type ==pg.QUIT:
             running=False
    screen.fill((0,0,0))
    player()
    pg.display.update()