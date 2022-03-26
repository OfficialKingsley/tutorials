import random


class Dice:
    def roll(self):
        for i in range(2):
            value1 = random.randint(1, 6)
            value2 = random.randint(1, 6)
            value_gotten = (value1, value2)
        return value_gotten


dice = Dice()
gotten = dice.roll()
print(gotten)
