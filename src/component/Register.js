import React from 'react';
import SignIn from './auth/SignIn';
import SignUp from './auth/Signup.js';
import { BrowserRouter, Routes, Route } from 'react-router-dom'; // Import the BrowserRouter, Routes, and Route components
const Register = () => {
    return (
        <>
        <div>
        <SignIn />
        </div>

     </>
    );
}

export default Register;