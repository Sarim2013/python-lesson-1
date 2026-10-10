import pgzrun
import random
from time import time

WIDTH = 800
HEIGHT = 800
TITLE = "Connecting Satellites"

satellites = []
lines = []
next_satellite = 0
number_of_satellite = 20

start_time = 0
end_time = 0
total_time = 0
game_over = False


def create_satellite():
    global start_time

    satellites.clear()
    lines.clear()

    for count in range(number_of_satellite):
        satellite = Actor("satellite")
        satellite.pos = (
            random.randint(40, WIDTH - 40),
            random.randint(40, HEIGHT - 50)
        )
        satellites.append(satellite)

    start_time = time()


def draw():
    screen.fill("black")

    # Draw connecting lines
    for line in lines:
        screen.draw.line(line[0], line[1], "white")

    # Draw satellites and their numbers
    for i, satellite in enumerate(satellites):
        satellite.draw()
        screen.draw.text(
            str(i + 1),
            (satellite.x + 15, satellite.y),
            color="yellow"
        )

    # Display elapsed time
    if not game_over:
        elapsed = time() - start_time
    else:
        elapsed = total_time

    screen.draw.text(
        f"Time: {elapsed:.2f} seconds",
        (20, 20),
        color="white",
        fontsize=30
    )

    if game_over:
        screen.draw.text(
            "You connected all satellites!",
            center=(WIDTH // 2, HEIGHT - 40),
            color="green",
            fontsize=30
        )


def update():
    pass


def on_mouse_down(pos):
    global next_satellite, end_time, total_time, game_over

    if game_over:
        return

    if next_satellite < number_of_satellite:
        satellite = satellites[next_satellite]

        if satellite.collidepoint(pos):
            if next_satellite > 0:
                previous = satellites[next_satellite - 1]
                lines.append((previous.pos, satellite.pos))

            next_satellite += 1

            if next_satellite == number_of_satellite:
                end_time = time()
                total_time = end_time - start_time
                game_over = True


create_satellite()

pgzrun.go()