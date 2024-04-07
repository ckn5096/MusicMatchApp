// Home.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from './AuthContext';
import { useNavigate } from 'react-router-dom';
import './Home.css'; // Import custom CSS for styling
<<<<<<< HEAD
import musicLogo from '../musicLogo.png';
import userLogo from '../userLogo.png';

=======
import musicLogo from '/Users/abimbolaoyewole/Desktop/MusicMatchAppV2/frontend/gui/src/Images/musicLogo.png';
import userLogo from '/Users/abimbolaoyewole/Desktop/MusicMatchAppV2/frontend/gui/src/Images/userLogo.png';
import HistoryLogo from '/Users/abimbolaoyewole/Desktop/MusicMatchAppV2/frontend/gui/src/Images/HistoryLogo.png';
>>>>>>> origin/master

const Home = () => {
    const [message, setMessage] = useState('');
    const { authToken, storedToken, logout } = useAuth();
    const navigate = useNavigate();

    const handleSignOut = () => {
        // Access the logout function from useAuth hook
        logout();
        navigate('/', { replace: true });
    };

    const goToProfileUpdate = () => {
        navigate('/profile/update'); // Navigate to the profile update page
    };

    const goToMusicPreferences = () => {
        navigate('/MusicPreference'); // Navigate to the music preferences page
    };

<<<<<<< HEAD
=======
     const goToListeningHistory = () => {
        navigate('/ListeningHistory'); // Navigate to the music preferences page
    };

>>>>>>> origin/master
    useEffect(() => {
        const fetchUserData = async () => {
            try {
                if (authToken) {
                    const response = await axios.get('http://127.0.0.1:8000/home/', {
                        headers: {
                            Authorization: `Bearer ${authToken}`,
                        },
                    });
                    setMessage(response.data.message);
                }

                if (storedToken) {
                    const response = await axios.get('http://127.0.0.1:8000/home/', {
                        headers: {
                            Authorization: `Bearer ${storedToken}`,
                        },
                    });

                    setMessage(response.data.message);
                }
                // Handle stored token if needed
            } catch (error) {
                console.error('Error fetching data!!:', error.response.data);
                navigate('/login', { replace: true }); // Redirect to login page if authentication fails
            }
        };

         if (authToken || storedToken) {
            fetchUserData();
            console.log('Auth token after login ' , authToken);
        }

        else{
           // console.log('Error fetching auth token');
            console.log('Error fetching auth token' , authToken);
           navigate('/login', { replace: true }); // Redirect to login page if authToken is not available
        }
    }, [authToken, storedToken,  navigate]);

    return (
        <div className="home-container">
            <h1 className="welcome-message">{message}</h1>
            {/* Add other stuff here for welcome */}

           {/* Container for Music Preferences button */}
            <div className="action-container">
                <div className="action-content">
                    <img src={musicLogo} alt="Icon" className="action-icon" />
                    <h2>Discover New Music</h2>
                    <p>Explore recommendations based on your preferences</p>
                    <button className="action-button" onClick={goToMusicPreferences}>Go to Discover</button>
                </div>
            </div>

<<<<<<< HEAD
=======
            {/* Container for Listening History button */}
            <div className="action-container">
                <div className="action-content">
                    <img src={HistoryLogo} alt="Icon" className="action-icon" />
                    <h2>Listening History</h2>
                    <p>View your listening history and analytics</p>
                    <button className="action-button" onClick={goToListeningHistory}>Go to Listening History</button>
                </div>
            </div>

>>>>>>> origin/master

            {/* Container for Profile Update button */}
            <div className="action-container">
                <div className="action-content">
                    <img src={userLogo} alt="Icon" className="action-icon" />
                    <h2>User Profile</h2>
                    <p>Manage account settings and update your personal information </p>
                    <button className="action-button" onClick={goToProfileUpdate}>Go to User Profile</button>
                </div>
            </div>

            {/* Add sign-out button */}
            <button className="sign-out-button" onClick={handleSignOut}>Sign Out</button>
        </div>
    );
};

export default Home;

