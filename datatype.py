
number = 67 #Integer
second = 45.98 #Float
greeting = "Hello there" #String
isPythonInteresting = True #Boolean

#Data structures - Multiple values stored in a single variable
cars = ["toyota","nissan","vw"] #list - Ordered and also changeable
fruits = ("banana","apple","mango") #Tuple- elements are ordered but unchangeable
countries = {"Kenya","Nigeria","Germany"} #set - elements are always unordered and also unchangeable
student = {
    "firstname" : "Jane",
    "age" : 25,
    "course" : "web Development",
    "gender" : "Female"
    }#Dictionary - Key-value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["gender"])


print(number)
print(second)
print(isPythonInteresting)


#Determining a datatype
print(type(countries))
print(type(student))

#Typecasting- converting one datatype to another
print(float(number))
print(int(second))
