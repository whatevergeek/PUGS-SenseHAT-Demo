from sense_hat import SenseHat
import requests

sense = SenseHat()
sense.clear()

service = 'http://<IP Address of your IR Emitter Webserver>/cmd?'

while True:
    accel = sense.get_accelerometer_raw()
    x = round(accel['x'])
    y = round(accel['y'])
    z = round(accel['z'])

    #motionless and flat sitting pi:
    # x will be 0
    # y will be 0
    # z will be 1

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    print("Accelerometer State: x=%s, y=%s, z=%s" % (x, y, z))

    if y == 1:
        #backward
        requests.get(service + 'led=1&mv=bwd')
    elif y == -1:
        #forward
        requests.get(service + 'led=1&mv=fwd')
    elif x == -1:
        #left
        requests.get(service + 'led=1&mv=left')
    elif x == 1:
        #right
        requests.get(service + 'led=1&mv=right')
    else:
        #stop
        requests.get(service + 'led=&mv=stop')