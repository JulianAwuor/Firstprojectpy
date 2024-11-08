temperature = 45

if temperature > 25:
    print("It is too hot")
else:
    print("It is too cold")


#A python program that checks three numbers and returns smallest number
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))


if first < second and first < third:
    print(first, "is th smallest number")
elif second < first and second < third:
    print(second, "is the smallest number")
else:
    print(third, "is the smallest number")


#Program to check whether a number is even or odd
number = 67

if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")