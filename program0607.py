#!/usr/bin/env pybricks-micropython
from common_calibration_001 import *

MyColorSensor.ID = 2

class Character:
    def __init__(self, name, hp, power, defense):
        self.name = name
        self.hp = hp
        self.power = power
        self.defense = defense
        
    def attack(self, target):
        # 物理攻撃の計算: 攻撃力 - 防御力（0以下なら0ダメージ）
        damage = max(0, self.power - target.defense)
        target.hp -= damage
        print("{}が{}に攻撃！ {}ダメージ与えた".format(self.name, target.name, damage))
        print("{}の体力: {}".format(target.name, target.hp))
        
    def recover(self):
        pass

class magic_Character(Character):
    def __init__(self, name, hp, power, defense, magic_power, magic_defense):
        super().__init__(name, hp, power, defense)
        self.magic_power = magic_power
        self.magic_defense = magic_defense
        
    def magic_attack(self, target):
        # 魔法攻撃の計算: 魔法攻撃力 - 魔法防御力（0以下なら0ダメージ）
        damage = max(0, self.magic_power - target.magic_defense)
        target.hp -= damage
        print("{}が{}に魔法攻撃！ {}ダメージ与えた".format(self.name, target.name, damage))
        print("{}の体力: {}".format(target.name, target.hp))

# モーター・センサー等の設定
motorA = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)
c1 = Color.WHITE
motorA.run(50)

# キャラクターの初期化
A = magic_Character("Human", 50, 30, 10, 40, 20)
B = magic_Character("Bird", 200, 20, 30, 10, 0)

while True:
    wait(50)
    c2 = tape_color(color_sensor)
    
    # 色の変化があった場合のみ処理
    if (not c1 == c2):
        if c2 == Color.RED:
            A.attack(B)
        elif c2 == Color.GREEN:
            B.attack(A)
        elif c2 == Color.BLUE:
            A.magic_attack(B)
        elif c2 == Color.YELLOW:
            B.magic_attack(A)
            
    # 終了判定
    if c2 == Color.BLACK or A.hp <= 0 or B.hp <= 0:
        break
        
    c1 = c2

# 勝敗判定
if A.hp <= 0 and B.hp <= 0:
    print("両者倒れました。引き分けです。")
elif A.hp <= 0:
    print("{}が勝利しました".format(B.name))
elif B.hp <= 0:
    print("{}が勝利しました".format(A.name))
else:
    print("決着がつきませんでした")