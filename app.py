from flask import Flask,render_template,request
import mysql.connector

app=Flask(__name__)
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="bTjJ@1211.6640",
    database="employeedetails"
)

mycursor=mydb.cursor()
usr_dict = {'admin':'pwd1','user1':'1234','user2':'4567'}

@app.route('/')
def login_page():
    return render_template('login.html')

# @app.route('/welcome',methods=['POST'])
# def welcome():
#     name=request.form['name']
#     return f'Welcome {name}!!'

# @app.route('/hello/<name>')
# def home_name(name):
#     return 'Hello %s!!!!' % name

# @app.route('/enter')
# def form_name():
#     return render_template('index.html')

@app.route('/home',methods=['POST'])
def home():
    usr_name=request.form['username']
    pswd=request.form['password']
    if usr_name not in usr_dict:
        return render_template('login.html',msg='Invalid Username')
    elif pswd!=usr_dict[usr_name]:
        return render_template('login.html',msg='Invalid Password')
    else:
        return render_template('home.html')

@app.route('/contactus')
def contactus_page():
    return render_template('ContactUs.html')

@app.route('/aboutus')
def aboutus_page():
    return render_template('AboutUs.html')

@app.route('/empDetails')
def empDetails_page():
    return render_template('empDetails.html')

@app.route('/searchEmp')
def searchEmp_page():
    return render_template('searchEmp.html')

# @app.route('/add')
# def add():
#     return render_template('add.html')

@app.route('/addemployee',methods=['GET','POST'])
def addemp():
    if request.method == 'POST':
        id=request.form.get('id')
        name=request.form.get('name')
        dep=request.form.get('dept')
        sal=request.form.get('salary')
        
        query="insert into emp_details values (%s, %s, %s, %s)"
        data = (id, name, dep, sal)
        mycursor.execute(query,data)
        mydb.commit()
        return render_template('home.html')
    return render_template('add.html')

@app.route('/view_all')
def view():
    query="select * from emp_details"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/searchresult',methods=['POST'])
def searchresult():
    ename=request.form.get('empname')
    query="SELECT * FROM emp_details WHERE emp_name LIKE f'%{ename}%' "
    mycursor.execute(query)
    data=mycursor.fetchall()
    if not data:
        return render_template('search.html', msg="Employee not Found")
    else:
        return render_template('view.html',sqldata=data)

if __name__ =='__main__':
    app.run(debug=True)
