#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
motorA.run(50)

while True:
    wait(50)
    c1 = tape_color(color_sensor)
    
    if c1 == Color.RED:
        brick.light(Color.RED)
    elif c1 == Color.YELLOW:
        brick.light(Color.YELLOW)
    elif c1 == Color.GREEN:
        brick.light(Color.GREEN)
    elif c1 == Color.BLUE:
        brick.light(Color.BLUE)
    elif c1 == Color.WHITE:
        brick.light(Color.WHITE)
    elif c1 == Color.BLACK:
        brick.light(Color.BLACK)