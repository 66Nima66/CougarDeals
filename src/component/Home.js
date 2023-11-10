/* eslint-disable no-undef */
/* eslint-disable no-unused-vars */

import React, { useState } from 'react';
import '../App.css';
import Header from './Header';
import Footer from './Footer';
import iphoneImage from '../images/iphone15.jpeg';
import productData from './back/Data/Data.js';

export const Home = () => {

  const websiteName = 'Cougar Deals';
  const products = [
    {
      name: productData[0].name,
      description: productData[0].description,
      applePrice: productData[0].manuFactorPrice,
      amazonPrice: productData[0].ourPrice,
      image: iphoneImage,
    },
    // Add more products here as needed
    {
      name: productData[1].name,
      description: productData[1].description,
      applePrice: productData[1].manuFactorPrice,
      amazonPrice: productData[1].ourPrice,
      image: iphoneImage,
    },
    {
      name: productData[2].name,
      description: productData[2].description,
      applePrice: productData[2].manuFactorPrice,
      amazonPrice: productData[2].ourPrice,
      image: iphoneImage,
    },
    {
      name: productData[3].name,
      description: productData[3].description,
      applePrice: productData[3].manuFactorPrice,
      amazonPrice: productData[3].ourPrice,
      image: iphoneImage,
    },
    // ... Add more products as needed
  ];

  // State for the wishlist
  const [wishlist, setWishlist] = useState([]);

  // Function to add a product to the wishlist
  const addToWishList = (product) => {
    setWishlist([...wishlist, product]);
  };

  // Add the search functionality here
  const [searchInput, setSearchInput] = useState('');
  const [searchResult, setSearchResult] = useState(products);
  const handleSearch = () => {
    const filteredProducts = products.filter((product) =>
      product.name.toLowerCase().split(' ').some((word) => word.includes(searchInput.toLowerCase()))
    );
    setSearchResult(filteredProducts);
  };

  return (
    <div className="App">
      <Header />
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search for products..."
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      <div className="product-container">
        {searchResult.map((product, index) => (
          <div className="product-slot" key={index}>
            <h2>{product.name}</h2>
            <img src={product.image || iphoneImage} alt={product.name} style={{ maxWidth: '100%', height: 'auto' }} />
            <p>{product.description}</p>
            <p>Manufacturer Price: {product.manuFactorPrice} $</p>
            <p>Our Price: {product.ourPrice} $</p>
            <button>Buy from Manufacturer</button>
            <button>Buy from Us</button>
            <button onClick={() => addToWishList(product)}>Add to Wishlist</button>
          </div>
        ))}
      </div>

      <Footer />
    </div>
  );
};

export default Home;