// Header.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom'; // Assuming you are using react-router-dom



export const Header = () => {
  
  return (
    
    <div className="App-header">
      
      <h1>Cougar Deals</h1>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          
          <li>
            <Link to="/WishList">Wish List</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Header;
