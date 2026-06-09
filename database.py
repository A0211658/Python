import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'Arati0211'  # Required for flashing messages
def get_db():
    '''database connection'''
    conn=sqlite3.connect('myproject.db')
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    '''create table'''
    with get_db() as conn:
       conn=get_db()
       conn.execute('''CREATE TABLE IF NOT EXISTS students
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     roll INTEGER NOT NULL,
                     marks INTEGER NOT NULL,
                     subject TEXT NOT NULL,
                     attendance INTEGER DEFAULT 0)''')
       conn.commit()
       conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)