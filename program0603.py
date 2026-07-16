#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
c1 = Color.WHITE
nR = 0
nG = 0
nB = 0
nY = 0
motorA.run(50)

while True:
    wait(50)
    c2 = tape_color(color_sensor)
    
    if (not c1 == c2):
        
            
        
            
        
            
            
                
                
                
                
                
                
        
            
    if c2 == Color.BLACK:
        
        break
    