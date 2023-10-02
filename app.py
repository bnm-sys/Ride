from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database initialization
conn = sqlite3.connect('rides.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rides (
        id INTEGER PRIMARY KEY,
        driver TEXT NOT NULL,
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book_ride', methods=['POST'])
def book_ride():
    if request.method == 'POST':
        driver = request.form['driver']
        origin = request.form['origin']
        destination = request.form['destination']
        date = request.form['date']
        time = request.form['time']

        conn = sqlite3.connect('rides.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO rides (driver, origin, destination, date, time) VALUES (?, ?, ?, ?, ?)',
                       (driver, origin, destination, date, time))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
