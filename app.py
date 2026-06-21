from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="studentdb"
)

@app.route('/')
def home():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('students.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    course = request.form['course']

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO students(name, course) VALUES(%s,%s)",
        (name, course)
    )
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)