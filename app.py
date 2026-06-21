from flask import Flask, render_template, request, redirect
import mysql.connector
import time

app = Flask(__name__)

def get_db_connection():
    for i in range(10):   # try 10 times
        try:
            db = mysql.connector.connect(
                host="db",
                user="root",
                password="root123",
                database="studentdb"
            )
            print("Connected to MySQL!")
            return db
        except mysql.connector.Error as err:
            print(f"MySQL not ready yet, retrying... {err}")
            time.sleep(5)
    raise Exception("Could not connect to MySQL after multiple retries")

db = get_db_connection()

@app.route('/')
def home():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    course = request.form['course']

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO students(name, course) VALUES(%s, %s)",
        (name, course)
    )
    db.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
