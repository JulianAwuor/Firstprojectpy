class Person:
    #Properties/Variables/Attribute/Characteristics
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    #Behavior/Method/Function
    def study(self):
        print("Student is studying")


 #Creating an object
student1 = Person("Hussein",23,"Male")
print(student1.name,student1.age,student1.gender)

student2 = Person("Alex",45,"Male")
print(student2.name,student2.age,student2.gender)

student3 = Person("Beatrice",34,"Female")