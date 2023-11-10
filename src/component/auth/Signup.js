import { createUserWithEmailAndPassword } from "firebase/auth";
import React, { useState } from "react";
import { auth } from "../../firebase";

const SignUp = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const signUp = (e) => {
        e.preventDefault();
        createUserWithEmailAndPassword(auth, email, password)
            .then((userCredential) => {
                // Sign up successful
                alert("Sign up successful!"); // Alert when sign up is successful
                console.log(userCredential);
            })
            .catch((error) => alert(error.message));
    };

    return (
        <div>
            <h1>Sign Up</h1>
            <form onSubmit={signUp}>
                <input
                    type="text"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => {
                        setEmail(e.target.value);
                    }}
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => {
                        setPassword(e.target.value);
                    }}
                />
                <button type="submit">Sign Up</button>
            </form>
        </div>
    );
};

export default SignUp;
