from sense_hat import SenseHat

sense = SenseHat()

sense.show_letter("i")

while True:
    y, x, z = sense.get_accelerometer_raw().values()

    x = round(x, 0)
    y = round(y, 0)

    if y == -1:
        sense.set_rotation(180)
    elif x == -1:
        sense.set_rotation(90)
    elif x == 1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)
