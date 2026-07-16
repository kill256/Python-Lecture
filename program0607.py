#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *
MyColorSensor.ID = 

class Character:
    def __init__(self,name,hp,power,defense):
        
        
        
        
    def attack(self,target):
        
            
        
            
        
        
    def recover(self):
        
        

class magic_Character(Character):
    def __init__(self,name,hp,power,defense,magic_power,magic_defense):
        
        
        
        
        
        
    def magic_attack(self,target):
        
            
        
            
        
        

motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
c1 = Color.WHITE
motorA.run(50)
A = 
B = 

while True:
    wait(50)
    c2 = tape_color(color_sensor)
    if (not c1 == c2):
        
            
        
            
        
            
        
            
        
            
    if c2 == Color.BLACK or 
        
        break
    c1 = c2

    print("{}が勝利しました".format(B.name))

    print("{}が勝利しました".format(A.name))

    print("決着がつきませんでした")
