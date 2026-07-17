#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
c1 = Color.WHITE
rev = 0
motorA.run(50)

while True:
    wait(50)
    c2 = tape_color(color_sensor)
    
    if (not c1 == c2) and (not c2 == Color.WHITE):
        if c2 == Color.RED:
            print('RED')
            if 
                
        elif c2 == Color.YELLOW:
            print('YELLOW')
            if 
                
        elif c2 == Color.GREEN:
            print('GREEN')
            if 
                
        elif c2 == Color.BLUE:
            print('BLUE')
            if 
                
    if c2 == Color.BLACK and 
        
        
        rev = 1
    elif c2 == Color.BLACK and 
        
        break
    