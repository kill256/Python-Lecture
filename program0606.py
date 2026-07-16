#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
touch_sensor = TouchSensor(Port.S2)
c1 = Color.WHITE
motorA.run(50)

while True:
    wait(50)
    c2 = tape_color(color_sensor)
    if (not c1 == c2) and (not c2 == Color.WHITE):
        
            
        
            
        
            
        
            
        
        
            
        
    if c2 == Color.BLACK:
        
        break
    