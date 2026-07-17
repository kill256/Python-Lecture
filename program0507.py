#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
c1 = Color.WHITE
motorA.run(50)

while True:
    wait(50)
    c2 = tape_color(color_sensor)
    
    if (not c1 == c2) and (not c2 == Color.WHITE):
        
        if c2 == Color.RED:
            brick.sound.beep(532,400,10)
        
        elif c2 == Color.YELLOW:
            brick.sound.beep(698,400,10)
        
        elif c2 == Color.GREEN:
            brick.sound.beep(587,400,10)
        
        elif c2 == Color.BLUE:
            brick.sound.beep(659,400,10)
    if c2 == Color.BLACK:
        
        break
    