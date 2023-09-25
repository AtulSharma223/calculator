class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        addition=self.a+self.b
        return addition
    def sub(self):
        substraction=self.a-self.b
        return substraction
    def mul(self):
        multiply=self.a*self.b
        return multiply
    def div(self):
        division=self.a//self.b
        return division
    
a=int(input("Enter a "))
b=int(input("Enter b "))

calculator1=calculator(a,b)
print("Addition is",calculator1.add())
print("substraction is",calculator1.sub())
print("Multiplication is",calculator1.mul())
print("Division is",calculator1.div())
