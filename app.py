# Store this code in 'app.py' file
  
from flask import Flask, render_template, request, redirect, url_for, session,flash,Markup
import mysql.connector
import requests
import json
import re

'''
THE MYSQL DATABASE = donate
Table = accounts

Create table accounts (

id int(10) not null auto_increment,
name varchar(150) not null,
Age int(100) not null,
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

chat = []


helpline = {

'Andhra Pradesh'    :'0866-2410978',
'Arunachal Pradesh' :'9436055743',
'Assam'             :'6913347770',
'Bihar'             :'104',
'Chhattisgarh'      :'104',
'Goa'               :'104',
'Gujarat'           :'104',
'Haryana'           :'8558893911',
'Himachal Pradesh'  :'104',
'Jharkhand'         :'104',
'Karnataka'         :'104',
'Kerala'            :'0471-2552056',
'Madhya Pradesh'    :'104',
'Maharashtra'       :'020-26127394',
'Manipur'           :'3852411668',
'Meghalaya'         :'108',
'Mizoram'           :'102',
'Nagaland'          :'7005539653',
'Odisha'            :'9439994859',
'Punjab'            :'104',
'Rajasthan'         :'0141-2225624',
'Sikkim'            :'104',
'Tamil Nadu'        :'044-29510500',
'Telangana'         :'104',
'Tripura'           :'0381-2315879',
'Uttarakhand'       :'104',
'Uttar Pradesh'     :'18001805145',
'West Bengal'       :'1800313444222,03323412600',
'Andaman and Nicobar Islands':'03192-232102',
'Chandigarh'        :'9779558282',
'Dadra and Nagar Haveli': '104',
'Delhi'             : '011-22307145',
'Jammu and Kashmir'   : '01912520982, 0194-2440283',
'Ladakh'            : '01982256462',
'Lakshadweep'       : '104',
'Daman and Diu'     : '104',
'Puducherry'        : '104',}








@app.route('/')
@app.route('/index', methods =['GET', 'POST'])





def index():

        
    session = requests.session()
    r = session.get("https://www.mohfw.gov.in/data/datanew.json").json()
    for i in r:
        scrap = []
        if i['sno'] == '11111':
            scrap.append([i["new_active"],i["new_positive"],i["new_cured"],int(i["new_active"])-int(i["active"]),int(i["new_positive"])-int(i["positive"]),int(i["new_cured"])-int(i["cured"])])
            
    return render_template('index.html',scrap=scrap)


@app.route('/state', methods =['GET', 'POST'])





def state():
    number = ''
    state = ''
    if request.method == 'POST' and 'state' in request.form:
        state = request.form['state']
        number =  'Helpline Number :'+helpline[state]
        state =" State:"+state
    return render_template('state.html',number = number,state =state)

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = 'Please Fill up the Form'
    array = ['','','','State','','Gender','Month','Year','','Blood Group']
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
        array = [name,age,city,state,email,gender,month,year,number,bloodgrp]

        if '' in array or 'State' in array or 'Blood Group' in array or 'Month' in array or 'Year' in array:
            msg = 'Please fill the form correctly'
        
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        else:
            cursor.execute("INSERT INTO accounts  VALUES (NULL,'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}');".format(name,age,city,state,email,gender,month,year,number,bloodgrp))
            cnx.commit()
            msg = 'You have successfully registered'
            array = ["","","","","","","","","",""]


    return render_template('register.html', msg = msg,array = array)


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
    
 
