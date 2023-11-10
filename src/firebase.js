// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import  { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC8xZ5BYbLo0DST4nat6DjHJyef-og3J6k",
  authDomain: "cougardeals-9b025.firebaseapp.com",
  projectId: "cougardeals-9b025",
  storageBucket: "cougardeals-9b025.appspot.com",
  messagingSenderId: "185260017609",
  appId: "1:185260017609:web:e5048e57b4d76aed1aca18",
  measurementId: "G-7YK1Z6C79Z"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(app);

export { auth };