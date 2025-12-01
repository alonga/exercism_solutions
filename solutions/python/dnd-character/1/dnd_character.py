import random
import math


def modifier(value):
    return math.floor((value - 10) / 2)


class Character:
    @staticmethod
    def ability():
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])   # drop the lowest die

    def __init__(self):
        self.strength = Character.ability()
        self.dexterity = Character.ability()
        self.constitution = Character.ability()
        self.intelligence = Character.ability()
        self.wisdom = Character.ability()
        self.charisma = Character.ability()
        self.hitpoints = 10 + modifier(self.constitution)
