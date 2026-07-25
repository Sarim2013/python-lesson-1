import pgzrun
from random import randint

WIDTH=600
HEIGHT=400
TITLE="Feed The Bee"
score=0


bee=Actor("bee")
bee.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))


pollen=Actor("pollen")
pollen.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))


def draw():
    global screen
    screen.blit("background",(0,0))
    bee.draw()
    pollen.draw()
    screen.draw.text(str(score), color="black",topleft=(10,10))

def update():
    global score
    if keyboard.w:
        bee.y-=10

    if keyboard.s:
        bee.y+=10


    if keyboard.a:
        bee.x-=10

    if keyboard.d:
        bee.x+=10

    if bee.colliderect(pollen):
        pollen.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))
        score+=1




pgzrun.go()