import pgzrun, random
from time import time
WIDTH=800
HEIGTH=800
TITLE = "Connecting Satellites"
satellites = []
lines = []
next_satellite = 0
number_of_satellite = 20

start_time = 0
end_time = 0
total_time = 0
def create_satellite():
    global start_time
    for count in range(0, number_of_satellite):
        satellite = Actor("satellite")
        satellite.pos = random.randint(40, WIDTH-40),random.randint(40, HEIGTH-50)
        satellites.append(satellite)
    start_time=time()

def draw():
    pass

def update():
    pass

def on_mouse_down(pos):
    pass



create_satellite()






pgzrun.go()