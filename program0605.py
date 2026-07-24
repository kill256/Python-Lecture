#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 140

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
touch_sensor = TouchSensor(Port.S2)
c1 = Color.WHITE
motorA.run(50)
rev = 0

while True:

    if rev == 0 and touch_sensor.pressed():

        motorA.run(-50) 
        rev = 1
        
    elif rev == 1 and not touch_sensor.pressed():

        motorA.run(50) 
        rev = 0 
        
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
            

    c1 = c2
        

    if c2 == Color.BLACK:
        motorA.stop(Stop.BRAKE)
        break