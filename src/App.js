import React from 'react';
import './App.css'; // Import your CSS file
import Home from './component/Home'; // Adjust the import path for the Home component
import { BrowserRouter, Routes, Route } from 'react-router-dom'; // Import the BrowserRouter, Routes, and Route components

function App() {
  
  return (
    
    <div>
    <BrowserRouter>
    <Routes>
      <Route index element = {<Home/>}/>
    </Routes>
    </BrowserRouter>
   </div>
    
  );
}

export default App;
