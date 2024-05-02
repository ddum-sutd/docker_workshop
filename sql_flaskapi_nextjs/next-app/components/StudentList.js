import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CreateStudentForm from './CreateStudentForm';

function StudentList() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData(); // Call fetchData function when component mounts
  }, []); // Empty dependency array ensures useEffect runs only once on mount

  const fetchData = async () => {
    try {
      const response = await axios.get('/api/student');
      setStudents(response.data || []);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching students:', error);
    }
  };


  const handleStudentCreated = async (newStudent) => {
    // Use a callback function to ensure you're updating based on the latest state
      fetchData(); // Refresh student list after creating a new student
  };
  

  return (
    <div>
      <CreateStudentForm onStudentCreated={handleStudentCreated} />
      <h2>Student List</h2>
      {loading ? (
        <div>Loading...</div>
      ) : (
        <div style={{ maxHeight: '400px', overflowY: 'auto' }}>
        <table className="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Age</th>
              <th>School</th>
            </tr>
          </thead>
          <tbody>
            {students.map((student) => (
                <tr key={student.id}>
                <td>{student.id}</td>
                <td>{student.name}</td>
                <td>{student.age}</td>
                <td>{student.school}</td>
                </tr>
            ))}
            </tbody>
        </table>
        </div>
      )}
    </div>
  );
}

export default StudentList;
