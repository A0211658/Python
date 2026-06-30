from flask import Flask, render_template,redirect,url_for
web=Flask(__name__,template_folder='webpages',static_folder='static')

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
    