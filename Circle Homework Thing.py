import pgzrun

WIDTH=400
HEIGHT=400


colors=["red","orange","yellow","green","blue","purple","violet"]

def draw():
    screen.fill("black")
    count=0
    for i in range(7,0,-1):
        screen.draw.filled_circle((200,200),2**i,colors[count])
        count+=1






pgzrun.go()