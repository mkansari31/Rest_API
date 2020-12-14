from flask import Flask, render_template , request,redirect
from flask_mysqldb import MySQL


app=Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        userdetails = request.form
        name = userdetails['name']
        email = userdetails['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO USERS(name, email) values(%s,%s)", (name,email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM USERS ")
    if result>0:
        userdetails = cur.fetchall()
        return render_template("users.html",userdetails = userdetails) 


if __name__ == ("__main__"):
    
    app.run(debug=True)