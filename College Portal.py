#It Is the mini project about College Smart Portal
Students=['Arati','Pavan','Aabhijit','Bhakti','Aanu']
rollno=[1111,2222,3333,4444,5555]
marks=[80,50,90,88,75]
attendance=[88,90,98,87,60]
notice=[
    "All students herby informed the PYTHON INTERNSHIP is start from 28th May"
    "This internship will be continue until the date 28th August"
    "After This internship you will get a CERTIFICATE."
    "Most Important you will get the EXPERINCE How Real IT Industry work on Projects."
]


def Student_login():
    name=input("Enter Student Name:")
    Rollno=int(input("Enter The Student Roll number:"))
    for i in range(len(Students)):
       
        if Students[i]==name and rollno[i]==Rollno:
            print("Login Successfully")
            print("----Welcome to our Python Internship Tranning----")
            print("****Student Details***")
            print("Name:",name)
            print("Roll No:",rollno[i])
            print("Marks:",marks[i])
            print("Attendance:",attendance[i])
            print("Notice Board")
            print(notice)
            return
    else:
            print("Login Unsuccessful")
            
Student_login()
