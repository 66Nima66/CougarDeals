import { signInWithEmailAndPassword } from "firebase/auth";
import React, { useState } from "react";
import { auth } from "../../firebase";
import { Link } from "react-router-dom";

const SignIn = () => {
    const nameOfWebsite = "Cougar Deals";
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const signIn = (e) => {
        e.preventDefault();
        signInWithEmailAndPassword(auth, email, password)
            .then((userCredential) => {
                alert("Sign in successful!");
                console.log(userCredential);
            })
            .catch((error) => {
                alert("Sign in failed. " + error.message);
            });
    };

    return (
        <div className="signin-container">
            <h1>{nameOfWebsite}</h1>
            <form className="signin-form" onSubmit={signIn}>
                <h2>Sign In</h2>
                <input
                    type="text"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Sign In</button>
                <br></br>
                <Link to="/SignUp">Don't have an account? Sign up here!</Link>
            </form>
        </div>
    );
};

export default SignIn;
