import pgzrun
from random import randint

WIDTH=800
HEIGHT=500
TITLE="Catch The Pearl"
score=0


diver=Actor("diver")
diver.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))


pearl=Actor("pearl")
pearl.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))


def draw():
    global screen
    screen.blit("bg",(0,0))
    diver.draw()
    pearl.draw()
    screen.draw.text(str(score), color="black",topleft=(10,10))

def update():
    global score
    if keyboard.w:
        diver.y-=10

    if keyboard.s:
        diver.y+=10


    if keyboard.a:
        diver.x-=10

    if keyboard.d:
        diver.x+=10

    if diver.colliderect(pearl):
        pearl.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))
        score+=1




pgzrun.go()