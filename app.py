from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'wfcuser'
app.config['MYSQL_PASSWORD'] = 'BootcampPass2025!'
app.config['MYSQL_DB'] = 'workforcedb'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        city = request.form.get('city')
        state = request.form.get('state')

        if first_name and last_name and email:
            cursor = mysql.connection.cursor()
            cursor.execute(
                'INSERT INTO registrations (first_name, last_name, email, city, state) '
                'VALUES (%s, %s, %s, %s, %s)',
                (first_name, last_name, email, city, state),
            )
            mysql.connection.commit()
            cursor.close()
            message = f'Thank you, {first_name}. Your registration has been received.'
        else:
            message = 'Please provide first name, last name, and email.'

    return render_template('index.html', message=message)

@app.route('/registrations')
def registrations():
    cursor = mysql.connection.cursor()
    cursor.execute(
        'SELECT first_name, last_name, email, city, state, submitted_at '
        'FROM registrations ORDER BY submitted_at DESC'
    )
    records = cursor.fetchall()
    cursor.close()
    return render_template('registrations.html', records=records)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
