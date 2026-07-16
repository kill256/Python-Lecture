#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
motorA.run(50)

while True:
    wait(50)
    
    c1 = tape_color(color_sensor)
    
    if c1 == Color.RED:
        print('RED')
    elif c1 == Color.YELLOW:
        print('YELLOW')
    elif c1 == Color.GREEN:
        print('GREEN')
    elif c1 == Color.BLUE:
        print('BLUE')
    elif c1 == Color.WHITE:
        print('WHITE')
    elif c1 == Color.BLACK:
        print('BLACK')