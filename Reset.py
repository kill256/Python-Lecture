#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
motorA.run(-100)

c1 = tape_color(color_sensor)

while True:
    wait(50)
    if c1 == Color.BLACK:
        motorA.stop(Stop.BRAKE)
        break
    
    c1 = c2