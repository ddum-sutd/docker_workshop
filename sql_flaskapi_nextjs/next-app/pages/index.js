
import React from 'react';
import styles from '@/styles/Home.module.css';
import StudentList from '../components/StudentList';

export default function Home() {
  return (
    <div
      className="wrapper"
      style={{
        backgroundImage: `url('/aqua.jpg')`,
        backgroundSize: '100% 100%'
      }}
    > 
    <div className={styles.main}>
    <StudentList />
    </div>
    </div>
  );
}