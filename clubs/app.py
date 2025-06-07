from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mem.html')  # Ensure this template exists

@app.route('/register', methods=['POST'])
def register():
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    place = request.form.get('place')
    date = request.form.get('date')
    dept = request.form.get('dept')
    year = request.form.get('year')
    clubs = request.form.getlist('clubs')  # Retrieves list of selected clubs
    message = request.form.get('message')

    clubs_joined = ', '.join(clubs)  # Convert list to comma-separated string

    # Database operation
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Digidara1000',
            database='club'
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO club_members (name, email, phone, place, date, dept, year, clubs, message)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (name, email, phone, place, date, dept, year, clubs_joined, message))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "An error occurred while inserting data into the database."
    finally:
        cursor.close()
        conn.close()

#     return redirect('/success')  # Redirect after successful submission

# @app.route('/success')
# def success():
#     return "🎉 Thank you for registering! We'll contact you soon."

if __name__ == '__main__':
    app.run(debug=True)
