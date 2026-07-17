#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2

sound = {Color.RED:523, Color.GREEN:587, Color.BLUE:659, Color.YELLOW:698}
motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
c1 = Color.WHITE
motorA.run(50)

while True:
    wait(50)
    c2 = tape_color(color_sensor)
    
    if c1 != c2:
        if c2 in sound:
            brick.sound.beep(sound[c2],400,10)

c1 = c2