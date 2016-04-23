### SenseHAT
#### A Short Overview
By Paul Amazona  
Presented at Python User Group Singapore  
on 18April2016

Summary of Files:

* SenseHat_PUGS_20160418.pdf: slides used during the presentation
* Source Code
    * Demo 1 - Runthrough of Features
        * Location of original reference material: http://bit.ly/1QF1U3B
        * As discussed in the presentation,  
        I've fixed the xyz accelerometer settings in the code  
        to get the expected behavior.
        * Please note that I've amended 13_joystick_screen.py also.  
        The original example uses pygame, but it didn't work for me.  
        Hence, I ended up using evdev instead.
    * Demo 2 - Flappy Astronaut Plus Plus
        * Location of original reference material: https://www.raspberrypi.org/learning/flappy-astronaut/
    * Demo 3 - Bot Driver
        * Please note that this needs to call a webserver of the robot car setup.  
        In my demo, I used NodeMCU as the webserver which uses an IR emitter to send command signals to the bot.  
        The robot setup can also be implemented in other variations as long as it accepts the webservice calls from the bot driver code. 
* Video Link: https://engineers.sg/video/python-for-rpi-sense-hat-python-sg--677
