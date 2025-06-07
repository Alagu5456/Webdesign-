from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mem.html')
@app.route('/mem')
def mem():
    return render_template('mem.html')
@app.route('/algu')
def algu():
    return render_template('algu.html')  # your form page
@app.route('/reg')
def reg():
    return render_template('reg.html')  # your form page
@app.route('/about')
def about():
    return render_template('about.html')  # your form page

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    place = request.form.get('place')
    date = request.form.get('date')
    dept = request.form.get('dept')
    year = request.form.get('year')
    clubs = request.form.getlist('clubs')
    message = request.form.get('message')

    clubs_joined = ', '.join(clubs)

    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Digidara1000',
            database='club'
        )
        cursor = conn.cursor()
        cursor.execute("""
    INSERT INTO club_members (name, email, phone, place, reg_date, department, year, clubs, message)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""", (name, email, phone, place, date, dept, year, clubs_joined, message))

        conn.commit()
        print("✅ Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"❌ MySQL Error: {err}")
        return f"<h2>Error inserting data: {err}</h2>"
    finally:
        cursor.close()
        conn.close()

    return redirect('/success')

@app.route('/success')
def success():
    return "<h1>🎉 Thank you for registering! We'll contact you soon.</h1>"

if __name__ == '__main__':
    app.run(debug=True)
