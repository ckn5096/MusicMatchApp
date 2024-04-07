import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate , Link } from 'react-router-dom';
import './Registration.css'; // Import the CSS file with styles

const Registration = () => {
    const [first_name, setFname] = useState('');
    const [last_name, setLname] = useState('');
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
     const navigate = useNavigate();
     const [message, setMessage] = useState('');


    const handleRegistration = async () => {
        try {
            const formData = new FormData();
            formData.append('first_name', first_name);
            formData.append('last_name', last_name);
            formData.append('email', email);
            formData.append('username', username);
            formData.append('password', password);




            const response = await axios.post('http://127.0.0.1:8000/api/register/', formData);
            if (response && response.data) {
                console.log('Registration successful', response.data);
                navigate('/', {replace: true});
            } else {
                console.error('Registration failed: No Data in response');
            }
        } catch (error) {

            if (error.response) {
                const {status, data} = error.response;

                if (status === 400 && data.email) {
                    console.error('Email already exists. Please try again.');
                    setMessage('Email already exists. Please try again.');
                } else if (status === 400 && data.username) {
                    console.error('Username already exists. Please try again.');
                     setMessage('Username already exists. Please try again.');
                } else {
                    console.error('Registration failed:', data);
                }
                console.error('Registration failed:', error.response ? error.response.data : error.message);
            }
        }
    };

    return (
        <div className="registration-container">
            <h1>Registration</h1>
            <div className="registration-form">
                <input type="text" placeholder="First Name" onChange={(e) => setFname(e.target.value)} />
                <input type="text" placeholder="Last Name" onChange={(e) => setLname(e.target.value)} />
                <input type="text" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
                <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />

                <button onClick={handleRegistration}>Register</button>
                {message && <p className="error-message">{message}</p>}
            </div>
            <div className="signin-link">
                <p>Already have an account? <Link to="/login">Sign in</Link></p>
            </div>
        </div>
    );
};

export default Registration;
