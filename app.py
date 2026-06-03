#flask-Flask is the web franework writte n in python.It is lightweight and easy.
#flask concept:
#Browser(chrome)--->Reuest--->Flask-->Python code
#Browser (chrome)-->Response-->flask-->Python code
#@app.route('/')--> This handles URL
#def home()-->This is function
#return. ...-->This will take to browser
from flask import Flask
app=Flask(__name__)

#project data-dictonary
stud=[
    {'name':'Subhdra','Rollno':111,'Marks':67},
    {'name':'Draupadi','Rollno':222,'Marks':87},
    {'name':'Radha','Rollno':333,'Marks':90},
    {'name':'Kumati','Rollno':444,'Marks':80}
]
@app.route('/')
def home():
    #creating using html
    html='<h1>College portal-Student</h1>'
    html += '<ul>'
    for student in stud:
        html += f"<li>{student['name']} - Roll:{student['Rollno']},Marks:{student['Marks']}</li>"
    html +='</ul>'
    return html 

@app.route('/about')
def about():
    return '<h1>You can do it</h1>'

@app.route('/students')
def students():
    return '<h1>Nothing is impossible</h1>'

if __name__=='__main__':
    app.run(debug=True)