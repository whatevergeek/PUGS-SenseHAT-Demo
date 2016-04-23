from sense_hat import SenseHat
from time import sleep
from random import randint
from threading import Thread

sense = SenseHat()
sense.clear()

## GLOBALS
flight_speed = 0.3
pipe_movement_speed = 1
pipe_production_speed = 5

game_over = False
BLACK = (0, 0, 0)
GREEN = (0, 150, 30)
BLUE = (0, 0, 255)
y = 4
direction = +1

def draw_column():
    global game_over
    x = 7
    gap = randint(1,6)
    while x >= 0 and not game_over:
        for led in range(8):
            sense.set_pixel(x, led, GREEN)
        sense.set_pixel(x,gap, BLACK)
        sense.set_pixel(x,gap-1, BLACK)
        sense.set_pixel(x,gap+1, BLACK)
        sleep(pipe_movement_speed)
        for led in range(8):
            sense.set_pixel(x, led, BLACK)
        if collision(x, gap):
            game_over = True
        x -= 1

def draw_columns():
    while not game_over:
        column = Thread(target=draw_column)
        column.start()
        sleep(pipe_production_speed)

def get_shake():
    global direction
    while not game_over:
        accel = sense.get_accelerometer_raw()
        x = round(accel['x'])
        y = round(accel['y'])
        z = round(accel['z'])

        #motionless and flat sitting pi:
        # x will be 0
        # y will be 0
        # z will be 1

        if y > 0:
            direction = -1
        else:
            direction = +1
            
def collision(x, gap):
    if x == 3:
        if y < gap -1 or y > gap +1:
            return True
    return False
        

columns = Thread(target=draw_columns)
columns.start()

shake = Thread(target=get_shake)
shake.start()

while not game_over:
    sense.set_pixel(3, y, BLUE)
    sleep(flight_speed)
    sense.set_pixel(3, y, BLACK)
    y += direction
    if y > 7:
        y = 7
    elif y < 0:
        y = 0

shake.join()
columns.join()

sense.show_message("Game Over!!!", text_colour=(255, 0, 0))

