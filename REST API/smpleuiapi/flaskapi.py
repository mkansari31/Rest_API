from flask import Flask,render_template, request,redirect
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'simpleflaskdb'
app.config['DEBUG'] = True

mysql = MySQL(app)
 
@app.route('/', methods = ['POST', 'GET'])
def form():
        
     
    if request.method == 'POST':
        userdetails = request.form
        Name = userdetails['name']
        Age = userdetails['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO student VALUES(%s,%s)''',(Name,Age))
        mysql.connection.commit()
        cursor.close()
        return redirect('/login')
    return render_template('form.html')

@app.route('/login', methods=['GET'])
def login():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM student ")
    if result>0:
        userdetails = cur.fetchall()
    return render_template("users.html",userdetails = userdetails) 



app.run(host='localhost', port=5000)
