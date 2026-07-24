#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 140

class Character:
    def __init__(self, name, hp, power, defense):
        self.name = name
        self.hp = hp
        self.power = power
        self.defense = defense
        
    def attack(self, target):

        damage = self.power - target.defense

        if damage < 0:
            damage = 0
        

        target.hp = target.hp - damage
        print("{}の攻撃！ {}に {} のダメージ！".format(self.name, target.name, damage))
        
    def recover(self):

        self.hp = self.hp + 20
        print("{}は回復魔法を唱えた！ HPが20回復した！".format(self.name))

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
c1 = Color.WHITE
motorA.run(50)

A = Character("Bird", 100, 25, 5)
B = Character("Humstar", 120, 20, 8)

while True:
    wait(50)
    c2 = tape_color(color_sensor)
    

    if (not c1 == c2) and (not c2 == Color.WHITE):
        

        if c2 == Color.RED:
            A.attack(B)
            
   
        elif c2 == Color.YELLOW:
            B.attack(A)
            

        elif c2 == Color.GREEN:
            A.recover()
            
 
        elif c2 == Color.BLUE:
            B.recover()
            

        print("{}：HP {} / {}：HP {}".format(A.name, A.hp, B.name, B.hp))
        

    c1 = c2
    

    if c2 == Color.BLACK or A.hp <= 0 or B.hp <= 0:
        motorA.stop(Stop.BRAKE)
        break


if A.hp <= 0 and B.hp <= 0:
    print("相打ち！決着がつきませんでした")
elif A.hp <= 0:
    print("{}が勝利しました".format(B.name))
elif B.hp <= 0:
    print("{}が勝利しました".format(A.name))
else:
    print("テープの終端に達したため、決着がつきませんでした")