import pgzrun
from random import randint

TITLE="Spongebob"
WIDTH=547
HEIGHT=350

sponge=Actor("spongebob")
sponge.pos=(randint(0,WIDTH),randint(0,HEIGHT))

def draw():
    screen.blit("spongebob_background",(0,0))
    sponge.draw()



def on_mouse_down(pos): #will check click
    if sponge.collidepoint(pos):
        sponge.x=randint(0,WIDTH)
        sponge.y=randint(0,HEIGHT)
pgzrun.go()