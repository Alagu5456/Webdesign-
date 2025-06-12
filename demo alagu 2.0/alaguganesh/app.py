from flask import Flask, request, redirect, render_template, url_for
import mysql.connector

app = Flask(__name__)

# ---------- Routes ----------
@app.route('/')
def home():
    return render_template('algu.html')

@app.route('/algu')
def algu():
    return render_template('algu.html')

@app.route('/mem')
def mem():
    return render_template('mem.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/success')
def success():
    return "<h1>🎉 Thank you for registering! We'll contact you soon.</h1>"

# ---------- Register Form Submission ----------
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
        print("✅ Data inserted successfully into database.")
    except mysql.connector.Error as err:
        print("❌ MySQL Error:", err)
        return f"<h2>Error inserting data: {err}</h2>"
    finally:
        cursor.close()
        conn.close()

    return redirect('/success')

# ---------- Club List View ----------
@app.route('/club_list')
def club_list():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Digidara1000',
            database='club'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clubs")
        club_data = cursor.fetchall()
    except mysql.connector.Error as err:
        return f"<h2>Error loading clubs: {err}</h2>"
    finally:
        cursor.close()
        conn.close()

    return render_template('club_list.html', club=club_data)

# ---------- Dummy Join Link Handler ----------
@app.route('/join/<int:club_id>')
def join_club(club_id):
    return f"<h1>Joining club with ID: {club_id}</h1>"

# ---------- Debug Route to View All Data (Optional) ----------
@app.route('/debug_data')
def debug_data():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Digidara1000',
            database='club'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM club_members")
        data = cursor.fetchall()
        return f"<pre>{data}</pre>"
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
