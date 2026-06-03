#College Smart Portal
#Main Entity Dictionary
Project_info=[
    {'Name':'Collge Smart portal',
     'Developer':'Arati',
     'language':'Python',
     'Database':'student records',
     'status':'Active'
     }
]
#Students record with Five Entity
students=[
   {'name':'Aabhi','Rollno':111,'Marks':89,'Attendence':'88%'} ,
   {'name':'Pavan','Rollno':222,'Marks':79,'Attendence':'78%'} ,
   {'name':'Aanu','Rollno':333,'Marks':98,'Attendence':'80%'} ,
   {'name':'Aabhimanyu','Rollno':444,'Marks':100,'Attendence':'100%'} ,
   {'name':'Utrra','Rollno':555,'Marks':67,'Attendence':'56%'} 
]

#Status Function
def get_status():
    return Project_info[0]['status']

Name_stud=input("Enter the student name:")
#Challenge-Sarech Record function
def search_records(nav):
    for student in students:
        if student['name']==Name_stud:
            print("*****Welcome to the College Smart portal*****")
            print("Student name:",student['name'])
            print("Student Rolno:",student['Rollno'])
            print("Student marks:",student['Marks'])
            break
    else:
        print("Student Record not found in the databse")

#Bonus-Secondary Dictionary
Teacher=[
    {'Name':'ShriKrishna','Id':101,'Sub':'Object oriented Programming','exp':5},
    {'Name':'Karn','Id':102,'Sub':'Java','exp':7},
    {'Name':'Arjun','Id':103,'Sub':'Python','exp':7},
    {'Name':'Bhim','Id':104,'Sub':'html','exp':10},
    {'Name':'Krishna','Id':105,'Sub':'javascipt','exp':18}
]

print("Project Status:",get_status())
#Print By Loop
for student in students:
    print(student)

#paasing parameter to the Search record function
search_records([Name_stud])