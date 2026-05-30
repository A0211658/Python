#List-one variable with multiple values
student =["Arati","Dhanushree","Satyarth","Shivaji","Pavan","Aabhijit"]
print(student)
print(student[3])
print(student[2])
print("Topper:",student[0])
print(student[1])
print(student[4])
print("More "+student[5])

#Loop-TO print all the elements in the list
for student_name in student:
    print(f"hello {student_name} welcome to python programming")

marks=[90,50,70,60,38]
for i in marks:
    if i>=90:
        print(f"Excellent! you got {i} marks")
    elif i>=60:
        print(f"Good you got {i} marks")
    elif i>=40:
        print(f"you are passed with {i} marks")
    else:
        print(f"Sorry you are failed with {i} marks")


for i in range(1,6):
    print(i)



'''function it is block of code which we write only once and whnwvere we need it
 we can call it multiple times'''

def greet(name):
    print(f"Hello {name} welcome to python programming")

for student_name in student:
   greet(student_name)