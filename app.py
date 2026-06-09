#flask-Flask is the web franework writte n in python.It is lightweight and easy.
#flask concept:
#Browser(chrome)--->Reuest--->Flask-->Python code
#Browser (chrome)-->Response-->flask-->Python code
#@app.route('/')--> This handles URL
#def home()-->This is function
#return. ...-->This will take to browser
from flask import Flask, flash, redirect, url_for,render_template,request

from database import get_db, init_db


app=Flask(__name__)
app.secret_key = 'Arati0211'  # Required for flashing messages

#project data-dictonary
stud=[
    {'name':'Subhdra','Rollno':111,'Marks':100},
    {'name':'Draupadi','Rollno':222,'Marks':99},
    {'name':'Radha','Rollno':333,'Marks':99},
    {'name':'Kumati','Rollno':444,'Marks':98}
]
@app.route('/')
def home():
    #creating using html
  
    return render_template('home.html', students=stud)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/students')
def students():
    return render_template('students.html', students=stud)

@app.route('/department')
def department():
    return render_template('department.html')

@app.route('/Add Students',methods=["GET","POST"])
def add_students():
    
    if request.method == "POST":

        name = request.form["Student_name"]
        marks = request.form["marks"]
        roll = request.form["roll"]
        subject=request.form["subject"]
        attendance=request.form["attendance"]
        
        # Validation
        if not name or not marks:
            flash("All fields are required!", "danger")
            return redirect(url_for("add_students"))
        conn=get_db()
        conn.execute('''INSERT INTO students 
                     (name, roll, marks, subject, attendance)
                     VALUES (?, ?, ?, ?, ?)''', (name, len(stud) + 100, int(marks), 'subject', int(attendance)))
        conn.commit()
        conn.close()
        

        marks = int(marks)

        new_student = {
            "Rollno": len(stud) + 100,
            "name": name,
            "Marks": marks,
            "subject":subject,
            "attendance":attendance

        }

        stud.append(new_student)

        flash(f"Student {name} added successfully!", "success")
        print(f"updated student List: {stud}")

        # return redirect(url_for("students.html"))

    return render_template("add_students.html")

if __name__=='__main__':
    init_db()
    app.run(debug=True)