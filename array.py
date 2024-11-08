courses = ["MIT","Cybersecurity","Datascience"]
print(courses)

#Accessing an element in array
print(courses[1])

#Looping through an element
for y in courses:
    print("courses is",y)

#Adding a new element
courses.append("Web Development")
print(courses)

#Deleting an element
courses.remove("MIT")
print(courses)