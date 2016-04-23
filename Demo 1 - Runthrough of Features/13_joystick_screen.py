from evdev import InputDevice, ecodes,list_devices
from select import select
from sense_hat import SenseHat

devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
	if dev.name == "Raspberry Pi Sense HAT Joystick":
		js = dev
				
sense = SenseHat()
sense.clear()

running = True
px = 0
py = 0
sense.set_pixel(px, py, 255, 255, 255)

while running:
	r, w, x = select([dev.fd], [], [],0.01)
	for fd in r:
		for event in dev.read():
			if event.type == ecodes.EV_KEY and event.value == 1:
				sense.set_pixel(px, py, 0, 0, 0)  # Black 0,0,0 means OFF
					    
				if event.code == ecodes.KEY_UP and py > 0:
					print("up")
					py = py - 1
				elif event.code == ecodes.KEY_LEFT and px > 0:
					print("left")
					px = px - 1
				elif event.code == ecodes.KEY_RIGHT and px < 7:
					print("right")
					px = px + 1
				elif event.code == ecodes.KEY_DOWN and py < 7:
					print("down")
					py = py + 1
				else:
					print("invalid stroke")
					
				sense.set_pixel(px, py, 255, 255, 255)
