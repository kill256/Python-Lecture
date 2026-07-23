#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2 

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)


c1 = Color.WHITE
red_count = 0
motorA.run(50)


while True:
    wait(50)
    c2 = tape_color(color_sensor)


    if (not c1 == c2) and (not c2 == Color.WHITE):
        if c2 == Color.RED:
            red_count += 1
        else:
            red_count = 0


        if red_count == 2:
            motorA.stop(Stop.BRAKE)
            brick.sound.beep(1000, 500)
            brick.light(Color.RED)
            break


        c1 = c2


    if c2 == Color.BLACK:
        motorA.stop(Stop.BRAKE)
        break