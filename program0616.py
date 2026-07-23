#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *


motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)


pA = 23
pB = 14 


def get_color_num(color):
    if color == Color.RED:
        return 1
    elif color == Color.GREEN:
        return 2
    elif color == Color.BLUE:
        return 3
    elif color == Color.YELLOW:
        return 4
    return 0

pA_reversed = (pA % 10) * 10 + (pA // 10)

# 初期変数
c1 = Color.WHITE
prev_num = 0 
state = 0 
motorA.run(50)

while True:
    wait(50)
    c2 = tape_color(color_sensor)

    if (not c1 == c2) and (not c2 == Color.WHITE):
        curr_num = get_color_num(c2)

        if curr_num != 0:
            pair = prev_num * 10 + curr_num
            print("Color:", c2, " Pair:", pair)

  
            if state == 0:
                if pair == pB:

                    state = 1
                    motorA.run(-50)
                    wait(200)


            elif state == 1:

                if pair == pA_reversed:

                    state = 2
                    motorA.run(50)
                    wait(200)

            prev_num = curr_num

        c1 = c2

    if c2 == Color.BLACK:
        motorA.stop(Stop.BRAKE)
        break