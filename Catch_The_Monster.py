import pgzrun
from random import randint

TITLE="Catch The Monster"
WIDTH=547
HEIGHT=350
score=0
monster=Actor("mons")
monster.pos=(randint(0,WIDTH),randint(0,HEIGHT))

def draw():
    screen.blit("space-background-image-2",(0,0))
    screen.draw.text(str(score),color="white",topleft=(10,10))
    monster.draw()



def on_mouse_down(pos): #will check click
    global score
    if monster.collidepoint(pos):
        score+=1
        monster.x=randint(0,WIDTH)
        monster.y=randint(0,HEIGHT)
pgzrun.go()