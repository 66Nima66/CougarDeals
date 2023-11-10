import React from 'react';
import './App.css'; // Import your CSS file
import Home from './component/Home'; // Adjust the import path for the Home component
import WishList from './component/WishList'; // Adjust the import path for the WishList component
import Register from './component/Register'; // Adjust the import path for the Register component
import { BrowserRouter, Routes, Route } from 'react-router-dom'; // Import the BrowserRouter, Routes, and Route components
import SignUp from './component/auth/Signup';
import SignIn from './component/auth/SignIn';
function App() {
  
  return (
    
    <div>
    <BrowserRouter>
    <Routes>
      <Route index element = {<Home/>}/>
      <Route path = "/WishList" element = {<WishList/>}/>
      <Route path = "/Register" element = {<Register/>}/>
      <Route path = "/SignIn" element = {<SignIn/>}/>
      <Route path = "/SignUp" element = {<SignUp/>}/>
    </Routes>
    </BrowserRouter>
   </div>
    
  );
}

export default App;
