from flask import Flask, render_template,redirect,url_for,flash,request
web=Flask(__name__,template_folder='webpages',static_folder='static')

web.secret_key="Arati2026"

students = [
    {"name": "Tanuja", "roll": 1, "marks": 85},
    {"name": "Pratiksha", "roll": 2, "marks": 78},
    {"name": "Shlok", "roll": 3, "marks": 92},
    {"name": "Lucky", "roll": 4, "marks": 65},
]

@web.route("/students")
def students_page():
    return render_template("students.html", students=students)

@web.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
       name = request.form["student_name"]
       marks = int(request.form["marks"])
       roll = int(request.form["roll"])
       Company = request.form["Company"]
       Package = int(request.form["Package"])
       branch=request.form['branch']

       if not name or not marks:
            flash("Please provide both name and marks", "danger")
            return render_template("add_students.html")

       students.append({
            "name": name,
            "marks": marks,
            "roll": roll,
            "branch":branch,
            "Company": Company,
            "Package": Package
        })

       flash(f"Student {name} added successfully!", "success")
       return redirect(url_for("students_page"))

    return render_template("add_students.html")

@web.route('/')
def home():
    return render_template('home.html')

@web.route('/about')
def about():
    return render_template('about.html')

@web.route('/department')
def department():
    return render_template('department.html')

@web.route('/computer')
def computer():
    return render_template('computer.html')

@web.route('/electrical')
def electrical():
    return render_template('electrical.html')

@web.route('/mechanical')
def mechanical():
    return render_template('mechanical.html')
   
if __name__ == "__main__":
    web.run(debug=True)
    