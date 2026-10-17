import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = "Shoot the bug"

BLUE=(0,0,255)
ship = Actor("galaga")
bug = Actor("bug")
ship.pos = (WIDTH//2, HEIGHT-60)
speed=10
bullets = []
enemies = []
enemies.append(bug)
enemies[-1].x = 100
enemies[-1].y = -100
score = 0
def displayScore():
    screen.draw.text(str(score),(100,30),fontsize=50)

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50

def update():
    global score
    if keyboard.a:
        ship.x -= 5
        if ship.x <= 0:
            ship.x = 0
    elif keyboard.d:
        ship.x += 5
        if ship.x <= WIDTH:
            ship.x = WIDTH

    for bullet in bullets:
        if bullet.y <= 0:
            bullets.append(bullet)
        else:
            bullet.y -= 10
    for enemy in enemies:
        enemy.y +=3
        if enemy.y >= HEIGHT:
            enemy.y = -10
            enemy.x=random.randint(20, WIDTH-20)
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 100
                sounds.eep.play()
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
    displayScore()
pgzrun.go()