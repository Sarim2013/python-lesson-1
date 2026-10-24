import pgzrun
import random

WIDTH=800
HEIGHT=700

ship = Actor("galaga")
bug = Actor("bug")

ship.pos = (WIDTH//2, HEIGHT-60)
speed = 2
bullets=[]
enemies=[]

for i in range(10):
    enemies.append(Actor("bug"))
    enemies[-1].x= 100 + 70 * i
    enemies[-1].y= -40

score=0
direction = 1

def displayScore():
    screen.draw.text(str((score),(100,300),fontsize=50)) #position of score
                     


def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-50

def update():
    global score
    global direction
    movedown = False 
    if keyboard.a:
        ship.x -= 5
        if ship.x <= 0:
            ship.x = 0
    #to make the ship move right
    elif keyboard.d:
        ship.x += 5
        if ship.x >= WIDTH:
            ship.x =WIDTH

    #to fire the bullets
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    #the movement of the bugs
    if len(enemies)>0 and (enemies[0].x < 20 or enemies[-1].x > WIDTH-30):
        moveDown = True
        direction = direction*(-1)
    for enemy in enemies:
        enemy.x += 5*direction
        if moveDown == True:
            enemy.y += 10
        #to check the collision between the bullet and the enemy
        for bullet in bullets:
            if enemy.colliderect(bullet):
                sounds.eep.play()
                score += 10
                bullets.remove(bullet)
                enemies.remove(enemy)
def draw():
    screen.clear()
    screen.fill((0,0,255))
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    ship.draw()
    displayScore.go()
pgzrun.go()