from sense_hat import SenseHat
import time

sense = SenseHat()

sense.show_letter(">")

angles = [0, 90, 180, 270, 0, 90, 180, 270]
for r in angles:
    sense.set_rotation(r)
    time.sleep(0.5)
