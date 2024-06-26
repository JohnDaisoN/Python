class Animal:
    def __init__(self, name):
        self.name = name
    def showname(self):
        print(self.name)
class Human:
    def __init__(self, n):
        self.n = n
        
    def define(self):
        print('I am a human and my name is', self.n)
class Man(Animal,Human):
    def __init__(self,name,n):
        self.name = name
        self.n = n

m = Man('Human','John')
m.showname()
m.define()




class Lion(Animal):
    def sound(self):
        print('I roar')

class Cub(Lion):
    pass

c = Cub('Lion')
c.sound()
c.showname()



        