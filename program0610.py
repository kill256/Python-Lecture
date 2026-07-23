#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 2

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
c1 = Color.WHITE
colors = [] 


motorA.run(50)


while True:
    wait(50)
    c2 = tape_color(color_sensor)


    if (not c1 == c2) and (not c2 == Color.WHITE):

        colors.append(c2)
        c1 = c2

        if len(colors) == 2:
            first_color = colors[0]
            second_color = colors[1]

            

            if first_color == Color.RED and second_color == Color.RED:
                brick.sound.beep(523, 400, 5)
            elif first_color == Color.RED and second_color == Color.BLUE:
                brick.sound.beep(554, 400, 5)
            elif first_color == Color.RED and second_color == Color.YELLOW:
                brick.sound.beep(587, 400, 5)
            elif first_color == Color.RED and second_color == Color.GREEN:
                brick.sound.beep(622, 400, 5)


            elif first_color == Color.BLUE and second_color == Color.RED:
                brick.sound.beep(659, 400, 5)
            elif first_color == Color.BLUE and second_color == Color.BLUE:
                brick.sound.beep(698, 400, 5)
            elif first_color == Color.BLUE and second_color == Color.YELLOW:
                brick.sound.beep(740, 400, 5)
            elif first_color == Color.BLUE and second_color == Color.GREEN:
                brick.sound.beep(784, 400, 5)


            elif first_color == Color.YELLOW and second_color == Color.RED:
                brick.sound.beep(831, 400, 5)
            elif first_color == Color.YELLOW and second_color == Color.BLUE:
                brick.sound.beep(880, 400, 5)
            elif first_color == Color.YELLOW and second_color == Color.YELLOW:
                brick.sound.beep(932, 400, 5)
            elif first_color == Color.YELLOW and second_color == Color.GREEN:
                brick.sound.beep(988, 400, 5)


            elif first_color == Color.GREEN and second_color == Color.RED:
                brick.sound.beep(1046, 400, 5)
            elif first_color == Color.GREEN and second_color == Color.BLUE:
                brick.sound.beep(1109, 400, 5)
            elif first_color == Color.GREEN and second_color == Color.YELLOW:
                brick.sound.beep(1175, 400, 5)
            elif first_color == Color.GREEN and second_color == Color.GREEN:
                brick.sound.beep(1245, 400, 5)


            colors.clear()


    if c2 == Color.BLACK:
        motorA.stop(Stop.BRAKE)
        break