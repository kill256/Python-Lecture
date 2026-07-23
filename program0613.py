#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2


motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)


c1 = Color.WHITE
order = 0  
x = 0 
op_color = None 
y = 0 


motorA.run(50)


while True:
    wait(50)
    c2 = tape_color(color_sensor)

    if (not c1 == c2) and (not c2 == Color.WHITE):
        order += 1


        if order == 1:
            if c2 == Color.RED:
                x = 1
            elif c2 == Color.GREEN:
                x = 2
            elif c2 == Color.BLUE:
                x = 3
            elif c2 == Color.YELLOW:
                x = 4


        elif order == 2:
            op_color = c2


        elif order == 3:

            if c2 == Color.RED:
                y = 1
            elif c2 == Color.GREEN:
                y = 2
            elif c2 == Color.BLUE:
                y = 3
            elif c2 == Color.YELLOW:
                y = 4


            result = 0
            if op_color == Color.RED:
                result = x + y
            elif op_color == Color.GREEN:
                result = x - y
            elif op_color == Color.BLUE:
                result = x * y
            elif op_color == Color.YELLOW:
                result = -(x * y)

            print(result)


            order = 0


        c1 = c2

    if c2 == Color.BLACK:
        motorA.stop(Stop.BRAKE)
        break