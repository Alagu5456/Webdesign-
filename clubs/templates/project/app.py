from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Digidara1000",  # Replace with your password
    database="s"
)
cursor = db.cursor()

@app.route('/')
def form():
    return render_template('studentinfo.html')


    return f"Student {name} added successfully!"
@app.route('/submit', methods=['POST'])
def submit():

    name=request.form['name']
    phno=request.form['phno']
    username = request.form['username']
    password = request.form['password']


    # Insert into MySQL database (students table)
    insert_query = "INSERT INTO stu (name,phno,username,password) VALUES (%s,%s, %s,%s)"
    cursor.execute(insert_query, (name,phno,username, password))
    db.commit()

    return f"User {username} logged in and added to DB successfully."


if __name__ == '__main__':
    app.run(debug=True)