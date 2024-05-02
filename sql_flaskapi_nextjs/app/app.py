from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import pooling
import os
#from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": [
    "http://localhost:3000",  # Add the origin of your Next.js application
    "http://next-app:3000",
    # Add any additional origins as needed
]}}, methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Content-Type", "Authorization"],
            supports_credentials=True)


# Function to get a sql connection
def get_mysql_connection():
    config = {
        'user': 'root',
        'password': 'root_pass',
        'host': 'db',
        'port': '3306',
        'database': 'studentdb'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    return connection,cursor

# Get all students
@app.route('/student', methods=['GET'])
def get_students():
    try:
        conn,cursor = get_mysql_connection()
        students = get_students_helper(cursor)
        return jsonify(students), 200
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()
        
def get_students_helper(cursor):
    cursor.execute("SELECT * FROM student")
    result = cursor.fetchall()
    students = [{'id': row[0], 'name': row[1], 'age': row[2], 'school': row[3]} for row in result] 
    return students        
 
def create_update_helper_(request, query, success_message):
    data = request.json
    name = data.get('name')
    age = data.get('age')
    school = data.get('school')
    if not all([name, age, school]):
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        conn, cursor = get_mysql_connection()
        if 'id' in request.view_args:  # For update operation
            cursor.execute(query, (name, age, school, request.view_args['id']))
        else:  # For create operation
            cursor.execute(query, (name, age, school))
        conn.commit()
        return jsonify({'message': success_message}), 200
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()
        
def create_update_helper(request, query, success_message):
    data = request.json
    name = data.get('name')
    age = data.get('age')
    school = data.get('school')
    if not all([name, age, school]):
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        conn, cursor = get_mysql_connection()
        if 'id' in request.view_args:  # For update operation
            cursor.execute(query, (name, age, school, request.view_args['id']))
        else:  # For create operation
            cursor.execute(query, (name, age, school))
        conn.commit()
        
        ## Fetch get students to check added or updated successfully
        students = None
        students = get_students_helper(cursor) 
        return jsonify({'message': success_message, 'students': students }), 200
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# Create a new student
@app.route('/student', methods=['POST'])
def create_student():
    query = "INSERT INTO student (name, age, school) VALUES (%s, %s, %s)"
    success_message = 'Student created successfully'
    return create_update_helper(request,query,success_message)
   
   
# Update a student
@app.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    query = "UPDATE student SET name=%s, age=%s, school=%s WHERE id=%s"
    success_message = 'Student updated successfully'
    return create_update_helper(request,query,success_message)
    
 
# Delete a student
@app.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        conn,cursor = get_mysql_connection()
        cursor.execute("DELETE FROM student WHERE id=%s", (id,))
        conn.commit()
        
        if cursor.rowcount == 0:
            return jsonify({'error': 'Student with ID {} not found'.format(id)}), 404
            
        ## Fetch get students to check the result
        students = None
        students = get_students_helper(cursor)
        return jsonify({'message': 'Student deleted successfully','students': students}), 200
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    # Bind to 0.0.0.0 and specify port
    app.run(debug=True, host='0.0.0.0', port=5000)
