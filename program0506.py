#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
c1 = Color.WHITE
motorA.run(50)

data = []

while True:
    wait(50)
    c2 = tape_color(color_sensor)
    
    if (not c1 == c2) and (not c2 == Color.WHITE):
        
        # 終端（黒）を検知した場合
        if c2 == Color.BLACK:
            motorA.stop(Stop.BRAKE)
            break

        else:
            data.append(c2)
            
    c1 = c2

for c in data:
    print(c)