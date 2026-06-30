import secrets
from flask import Flask,render_template,request,redirect,url_for,session,flash
app=Flask(__name__)
app.secret.key=secrets.token_hex(16)

@app.route('/')
def home():
    name=session.get('name')
    return render_template('home.html',name=name)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name'.strip()]

        if not name:
            flash(f'Name is Required')
            return render_template('register.html')
        session['name']=name
        flash(f"welcome {name} ")
        return redirect(url_for('home'))
    return render_template('register.html')
        
