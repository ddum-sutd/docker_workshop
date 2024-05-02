// CreateStudentForm.js
import React, { useState } from 'react';
import axios from 'axios';

function CreateStudentForm({ onStudentCreated }) {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [school, setSchool] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    console.log('Name:', name);
    console.log('Age:', age);
    console.log('School:', school);
    
    try {
      const response = await axios.post(
        '/api/student',
        {
          name,
          age,
          school
        },
        {
          headers: {
            'Content-Type': 'application/json'
          }
        }
      );
      
      console.log('Student created successfully:', response.data);

      // Notify parent component that a new student is created
      onStudentCreated(response.data);

      // Reset form fields
      setName('');
      setAge('');
      setSchool('');
    } catch (error) {
      console.error('Error creating student:', error);
      setErrorMessage('Error creating student. Please try again.');
    }
  };

  return (
    <div className="flex-container" style={{ width: "500px", marginBottom: "1rem" }}>
      <h2>Create Student</h2>
      {errorMessage && <p className="text-danger">{errorMessage}</p>}
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="name" className="form-label">Name:</label>
          <input type="text" className="form-control" id="name" value={name} onChange={(e) => setName(e.target.value)} required />
        </div>
        <div className="mb-3">
          <label htmlFor="age" className="form-label">Age:</label>
          <input type="number" className="form-control" id="age" value={age} onChange={(e) => setAge(e.target.value)} required />
        </div>
        <div className="mb-3">
          <label htmlFor="school" className="form-label">School:</label>
          <input type="text" className="form-control" id="school" value={school} onChange={(e) => setSchool(e.target.value)} required />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>
    </div>
  );
}

export default CreateStudentForm;
