#Built-In Library Functions

y = max(34, 78, 56, 10)
print(y)

x = min(45, 90, 65, 43)
print(x)

z = pow(2, 3)
print("The result is",z)

#User-Defined Functions
def greeting():
    print("Hello there")

greeting() #Calling a function

def add():
    num1 = 7
    num2 = 20
    print(num1 + num2)

add()

#Parameter/Variable and Argument/value
def multipy(x,y):
    print(x * y)

multipy(5,34)
multipy(12,5)
multipy(46,3)

def doctor(name):
    print(name)

doctor("Joe")
doctor("Mary")
doctor("Clinton")


