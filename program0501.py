#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 140

motorA = Motor(Port.A)
motorA.run(50)

while True:
    wait(50)