#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
c1 = Color.WHITE
motorA.run(50)

while True:
    wait(50)
    
    c2 = tape_color(color_sensor)
    if (not c1 == c2) and (not c2 == Color.WHITE):
        
        if c2 == Color.RED:
            print('RED')
        elif c2 == Color.YELLOW:
            print('YELLOW')
        elif c2 == Color.GREEN:
            print('GREEN')
        elif c2 == Color.BLUE:
            print('BLUE')
    if c2 == Color.BLACK:
        motorA.stop(Stop.BRAKE)
        break