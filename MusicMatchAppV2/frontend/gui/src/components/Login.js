import React, { useState } from 'react';
import {Link, useNavigate} from 'react-router-dom';
import axios from 'axios';
import { useAuth } from './AuthContext';
import './Login.css';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate();
     const { login } = useAuth();


    const handleLogin = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/login/', {
                username: username,
                password: password,
            });

            const token = response.data.token;
            login(token);
            //document.cookie = `authToken=${authToken}; path=/`;
            // Save the token to localStorage or cookies

            console.log('Login successful');
             navigate(response.data.redirect_url);
        } catch (error) {
            console.error('Login failed:', error.response.data);
            setErrorMessage('Invalid username or password. Please try again.');

        }
    };

    return (
        <div className="login-container"> {/* Apply login container class */}
            <div className="login-form"> {/* Apply login form class */}
                <h1>Log In</h1>
                <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
                <button onClick={handleLogin}>Login</button>
                {errorMessage && <div className="error-message">{errorMessage}</div>}
                <div className="signup-link"> {/* Apply signup link class */}
                    <p>Need an account? <Link to="/registration">Sign up</Link></p>
                </div>
            </div>
        </div>
    );
};

export default Login;
