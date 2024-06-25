class calculations:
    def __init__(self,a,b) -> None:
        print('I am a constructor')
        print(a,b)
        self.a, self.b = a,b
    def add(self):
        #self.a_r = a + b
        
        return self.a + self.b
    def sub(self):
        #self.s_r = a - b
        # self.c = c
        # self.d = d
        return self.a - self.b
    def prod(self):
        #self.p_r = self.a_r * self.s_r
        return self.add() * self.sub()
    def div(self):
        #....
        return (self.add() + self.sub()) / self.prod()
    def display(self):
        #print(self.a_r, self.s_r,self.p_r, self.d_r)
        print('the sum of the numbers is', self.add())
        print('the difference of the numbers is', self.sub())
        print('the product of the numbers is', self.prod())
        print('the quotient of the numbers is', self.div())

c = calculations(2,3)
c.display()

