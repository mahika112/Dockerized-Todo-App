from flask import Flask, render_template, request, redirect
import mysql.connector 
import os 

app = Flask(__name__)

# Database connection
def get_db_connection():
    # Read connection details from environment variables
    return mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST', 'db'),        # Defaults to 'db'
        user=os.environ.get('MYSQL_USER', 'root'),
        password=os.environ.get('MYSQL_PASSWORD', 'root'),
        database=os.environ.get('MYSQL_DATABASE', 'todo_db')
    )
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS todos (id INT AUTO_INCREMENT PRIMARY KEY, task VARCHAR(255))")
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

