class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num2 + self.num1)


    def subtract(self):
        return (self.num2 - self.num1)

    def multiply(self):
       return (self.num2 * self.num1)

    def divide(self):
        return (self.num2 / self.num1)

cal = Calculator(10,24)
print("Addition is : ",cal.add())
print("Substraction :",cal.subtract())
print("Multiplication : ",cal.multiply())
print("Division : ",cal.divide())
