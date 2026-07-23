#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2


motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)


c1 = Color.WHITE
total_score = 0
sign = 1 


motorA.run(50)


while True:
    wait(50)
    c2 = tape_color(color_sensor)


    if (not c1 == c2) and (not c2 == Color.WHITE):


        if c2 == Color.BLUE:
            sign *= -1


        elif c2 == Color.RED:
            total_score += 1 * sign
            
        elif c2 == Color.GREEN:
            total_score += 2 * sign
            
        elif c2 == Color.YELLOW:
            total_score += 3 * sign
            


        c1 = c2


    if c2 == Color.BLACK:
        motorA.stop(Stop.BRAKE)
        break


print("Total: " + str(total_score))