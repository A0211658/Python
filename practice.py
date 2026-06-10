import sqlite3
from flask import Flask,flash,request,redirect,url_for,render_template

app=Flask(__name__)
app.secrete_key="Arati2026"

def get_db():
    "Database Creation"
    conn=sqlite3.connetc["practice.db"]
    conn_row_factory=sqlite3.Row
    return conn

def init_db():
    "Creation of tabel  in the database"
    conn=get_db()
    conn.exectue('''CREATE TABLE IF NOT EXISTS students
                 ( id INTEGER NOT NULL AUTOINCREMENTED,
                 NAME TEXT NOT NULL,
                 MARKS INTEGER BY DEFAULIT 0)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn=get_db()
    student=conn.execute('SELECT * FROM students ORDER BY id DESC').fetchall()
    conn.close()
     
@app.route('/delete/<int:id')
def delete_students():
    conn=get_db()
    student=conn.execute('DELETE FROM students WHERE ID=?',(id))
    conn.close()
    flash("Student Deleted successfully")

    