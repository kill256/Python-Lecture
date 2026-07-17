#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2

motorA = Motor(Port.A)
motorA.run(-50)

while True:
    wait(50)
    if c1 == Color.BLACK:
        motorA.stop(Stop.BRAKE)
        break