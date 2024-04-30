#https://stackoverflow.com/questions/45658144/connecting-to-mysql-from-flask-application-using-docker-compose
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import pooling
import os

app = Flask(__name__)

# Function to get a connection from the pool
def get_mysql_connection():
    config = {
        'user': 'root',
        'password': 'root_pass',
        'host': 'db',
        'port': '3306',
        'database': 'student_flask'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    return connection,cursor

# Create a new student
@app.route('/student', methods=['POST'])
def create_student():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    school = data.get('school')
    if not all([name, age, school]):
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        conn,cursor = get_mysql_connection()
        cursor.execute("INSERT INTO student (name, age, school) VALUES (%s, %s, %s)", (name, age, school))
        conn.commit()
        return jsonify({'message': 'Student created successfully'}), 201
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Get all students
@app.route('/student', methods=['GET'])
def get_students():
    
    try:
        conn,cursor = get_mysql_connection()
        cursor.execute("SELECT * FROM student")
        result = cursor.fetchall()
        students = [{'id': row[0], 'name': row[1], 'age': row[2], 'school': row[3]} for row in result]
        return jsonify(students), 200
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Update a student
@app.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    name = data.get('name')
    age = data.get('age')
    school = data.get('school')
    if not all([name, age, school]):
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        conn,cursor = get_mysql_connection()
        cursor.execute("UPDATE student SET name=%s, age=%s, school=%s WHERE id=%s", (name, age, school, id))
        conn.commit()
        return jsonify({'message': 'Student updated successfully'}), 200
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Delete a student
@app.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        conn,cursor = get_mysql_connection()
        cursor.execute("DELETE FROM student WHERE id=%s", (id,))
        conn.commit()
        return jsonify({'message': 'Student deleted successfully'}), 200
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    # Bind to 0.0.0.0 and specify port
    app.run(debug=True, host='0.0.0.0', port=5000)
