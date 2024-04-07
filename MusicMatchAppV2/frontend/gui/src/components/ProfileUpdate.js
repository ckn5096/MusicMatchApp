import React, { useState } from 'react';
import axios from 'axios';
import { useAuth } from './AuthContext';
import {useNavigate} from "react-router-dom";
import './ProfileUpdate.css';

const ProfileUpdate = () => {
    const [newUsername, setNewUsername] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [newFirstname, setNewFirstname] = useState('');
    const [newLastname, setNewLastname] = useState('');
    const [newEmail, setNewEmail] = useState('');
    const { authToken , storedToken, logout } = useAuth();
    const navigate = useNavigate();

    const handleSignOut = () => {
        // Access the logout function from useAuth hook
        logout();

        navigate('/', {replace: true});
    };

    const handleUpdateProfile = async () => {
        try {
            const formData = new FormData();
            formData.append('new_username', newUsername);
            formData.append('new_password', newPassword);
            formData.append('new_firstname', newFirstname);
            formData.append('new_lastname', newLastname);
            formData.append('new_email', newEmail);

            const response = await axios.post('http://127.0.0.1:8000/profile/update/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    Authorization: `Bearer ${storedToken}`,
                },
            });


            navigate(response.data.redirect_url);
            console.log('Profile updated successfully:', response.data);
        } catch (error) {
            console.error('Error updating profile:', error.response.data);
        }
    };



     return (
        <div className="container"> {/* Add container class */}
            <h2>Update Profile</h2>
            <input type="text" placeholder="New Username" value={newUsername} onChange={(e) => setNewUsername(e.target.value)} />
            <input type="password" placeholder="New Password" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} />
            <input type="text" placeholder="New First Name" value={newFirstname} onChange={(e) => setNewFirstname(e.target.value)} />
            <input type="text" placeholder="New Last Name" value={newLastname} onChange={(e) => setNewLastname(e.target.value)} />
            <input type="text" placeholder="New Email" value={newEmail} onChange={(e) => setNewEmail(e.target.value)} />
            <button onClick={handleUpdateProfile}>Update Profile</button>
            <button onClick={() => navigate('/home')}>Home</button> {/* Add Home button */}
        </div>
    );
};

export default ProfileUpdate;
