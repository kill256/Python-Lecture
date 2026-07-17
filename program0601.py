#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
n = 5
c1 = Color.WHITE
motorA.run(50)

while True:
    wait(50)
    
    c2 = tape_color(color_sensor)
    if (not c1 == c2) and (not c2 == Color.WHITE):
        
        if c2 == Color.BLACK:
            motorA.stop(Stop.BRAKE)
        break
    
    else:
        n = n - 1
        if n == 0:
            motorA.stop(Stop.BRAKE)
            break
            print(c2)
        c1 = c2