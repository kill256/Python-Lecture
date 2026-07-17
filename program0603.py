#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2

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
    

    if (not c1 == c2) and (not c2 == Color.WHITE):
        
        if c2 == Color.RED:
            nR = nR + 1
        elif c2 == Color.GREEN:
            nG = nG + 1
            
        elif c2 == Color.BLUE:
            nB = nB + 1
  
            if nB == 3: 
                motorA.stop(Stop.BRAKE) 
                break
                
        elif c2 == Color.YELLOW:
            nY = nY + 1
            

        elif c2 == Color.BLACK:
            motorA.stop(Stop.BRAKE)
            break
            

    c1 = c2


print("Red: "+str(nR))
print("Green: "+str(nG))
print("Blue: "+str(nB))
print("Yellow: "+str(nY))