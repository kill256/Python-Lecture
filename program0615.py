#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)

c1 = Color.WHITE
blue_flag = False

motorA.run(50)


while True:
    wait(50)
    c2 = tape_color(color_sensor)


    if (not c1 == c2) and (not c2 == Color.WHITE):


        if c2 == Color.BLUE:
            if not blue_flag:
                # 【1回目の青】
                blue_flag = True

                motorA.run(-50)

                wait(200)
                while True:
                    c_back = tape_color(color_sensor)
                    if c_back != Color.WHITE:
                        break
                    wait(50)


                print(c_back)
                
                motorA.run(50)
                c1 = c_back

            else:
                blue_flag = False
                c1 = c2

        else:
            print(c2)
            c1 = c2

    if c2 == Color.BLACK:
        motorA.stop(Stop.BRAKE)
        break