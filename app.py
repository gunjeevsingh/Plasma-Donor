# Store this code in 'app.py' file
  
from flask import Flask, render_template, request, redirect, url_for, session,flash
import mysql.connector

import re
  
'''
THE MYSQL DATABASE = donate
Table = accounts

Create table accounts (

id int(10) not null auto_increment,
name varchar(150) not null,
Age int(100) not null,
Sex varchar(225) not null,
City varchar(100) not null,
state varchar(100) not null,
email varchar(100) not null,
gender varchar(10) not null,
month_of_recovery varchar(15) not null,
year_of_recovery varchar(10) not null,
Contact_Number varchar(14) not null,
blood_group varchar(3) NOT NULL,
Primary key (id)

)




'''
app = Flask(__name__)
app.secret_key = 'your secret key'
cnx = mysql.connector.connect(user='root', password='helloworld',
                              host='localhost',
                              database='donate')  
cursor = cnx.cursor()
@app.route('/')
@app.route('/index', methods =['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = 'Please Fill up the Form'
    if request.method == 'POST' and 'BloodGroup' in request.form:
        email     = request.form['email']
        name      = request.form['name']
        age       = request.form['age']
        gender    = request.form['gender']
        city      = request.form['city']
        state     = request.form['state']
        bloodgrp  = request.form['BloodGroup']
        number    = request.form['number']
        year      = request.form['year']
        month     = request.form['month']
        array = (name,age,city,state,email,gender,month,year,number,bloodgrp)
        cursor.execute("INSERT INTO accounts  VALUES (NULL,'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}');".format(name,age,city,state,email,gender,month,year,number,bloodgrp))
        cnx.commit()
        msg = 'You have successfully registered'
    


    return render_template('register.html', msg = msg)


@app.route('/View', methods =['GET', 'POST'])
def view():
    msg = ''
    if request.method == 'POST' and 'state' in request.form :
        city = request.form['state']

        
        cursor.execute("SELECT name,Age,blood_group,City,Contact_Number FROM accounts WHERE state = '{}';".format(city))
           

        data = cursor.fetchall()
        
        return render_template('View.html', data = data, msg = msg)

    elif request.method == 'POST':
        msg = 'Please fill out the details !'
    return render_template('View.html', msg = msg)



if __name__ == "__main__":
    app.run(host = "127.0.0.1",debug = True)
    
'''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM data WHERE city = '{}' AND dept = '{}';".format(city,dept))
'''  
