from random import randint
class Die:
    def __init__(self):
        self.sides = 6
        
    def roll_die(self):
        self.value = randint(1,self.sides)
        print(f"The fallen number will be {self.value}")

die1 = Die()
for i in range(1,11):
    die1.roll_die()


