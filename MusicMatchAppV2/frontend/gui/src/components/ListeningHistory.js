// import React , { useState, useEffect } from 'react';
// import axios from 'axios';
// import { useNavigate } from 'react-router-dom';
// import {useAuth} from "./AuthContext";
//
// const ListeningHistory = () => {
//     const navigate = useNavigate();
//     const {storedToken} = useAuth();
//     const [recentlyPlayed, setRecentlyPlayed] = useState([]);
//
//     // Function to handle Spotify login
//     const handleSpotifyLogin = async () => {
//         try {
//
//             // Make GET request to your SpotifyLoginView endpoint
//             const response = await axios.get('http://127.0.0.1:8000/api/Spotify/login');
//
//             // // Redirect user to Spotify login page
//
//
//             window.open(response.data.auth_url, '_blank');
//             // window.location.href = response.data.auth_url; // Assuming your backend returns the authorization URL
//         } catch (error) {
//             console.error('Error logging in with Spotify:', error);
//             // Handle error if necessary
//         }
//     };
//
//     // Function to handle fetching listening history
//     const handleListeningHistory = async () => {
//         try {
//
//              const config = {
//             headers: {
//                 Authorization: `Bearer ${storedToken}`,
//             }
//         };
//             // Make GET request to your ListeningHistoryView endpoint
//             const response = await axios.get('http://127.0.0.1:8000/api/ListeningHistory/' , config);
//
//             // Log the listening history data to the console
//             console.log('Listening History:', response.data);
//             // You can process the data further or display it as needed
//
//              // Update state with the recently played tracks
//             setRecentlyPlayed(response.data.tracks);
//
//         } catch (error) {
//             console.error('Error fetching listening history:', error);
//             // Handle error if necessary
//         }
//     };
//
//     // Fetch listening history when the component mounts
//     useEffect(() => {
//         handleListeningHistory();
//     }, []); // Empty dependency array ensures the effect runs only once, on component mount
//
//     return (
//         <div>
//             <h1>Listening History</h1>
//             {/* Button to initiate Spotify login */}
//             <button onClick={handleSpotifyLogin}>Login with Spotify</button>
//             {/* Button to fetch listening history */}
//             <button onClick={handleListeningHistory}>Fetch Listening History</button>
//             {/* Display recently played tracks */}
//             {recentlyPlayed.length > 0 &&
//                 <div>
//                     <h2>Recently Played Tracks</h2>
//                     <ul>
//                         {recentlyPlayed.map((track, index) => (
//                             <li key={index}>
//                                 <p>Track: {track.track_name}</p>
//                                 <p>Artist: {track.artist_name}</p>
//                                 <p>Album: {track.album_name}</p>
//                                 <p>Played At: {track.played_at}</p>
//                             </li>
//                         ))}
//                     </ul>
//                 </div>
//             }
//         </div>
//     );
// };
//
// export default ListeningHistory;

import React , { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from "./AuthContext";
import './ListeningHistory.css'; // Import CSS file for styling


const ListeningHistory = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const { storedToken, setStoredToken } = useAuth();
    const [recentlyPlayed, setRecentlyPlayed] = useState([]);

    // Function to handle Spotify login
    const handleSpotifyLogin = async () => {
        try {
            // Make GET request to your SpotifyLoginView endpoint
            const response = await axios.get('http://127.0.0.1:8000/api/Spotify/login');

            // Redirect user to Spotify login page
            window.open(response.data.auth_url, '_blank');
        } catch (error) {
            console.error('Error logging in with Spotify:', error);
            // Handle error if necessary
        }
    };

    // Function to handle fetching listening history
    const handleListeningHistory = async () => {
        try {

             // Get the access token from local storage
        const accessToken = localStorage.getItem('spotify_access_token');
        const tokenExpiry = localStorage.getItem('spotify_token_expiry');

            const config = {
                headers: {
                    Authorization: `Bearer ${storedToken}`,
                }
            };


            // // Make GET request to your ListeningHistoryView endpoint
            // const response = await axios.get('http://127.0.0.1:8000/api/ListeningHistory/', config);

             // Make GET request to your ListeningHistoryView endpoint with access token as query parameter
         const response = await axios.get('http://127.0.0.1:8000/api/ListeningHistory/', {
            params: {
                access_token: accessToken,
                token_expiry: tokenExpiry,
                accessToken: accessToken // Include storedToken as a parameter
            },
            headers: config.headers // Pass headers separately
        });
            // Log the listening history data to the console
            console.log('Listening History:', response.data);

            // Update state with the recently played tracks
            setRecentlyPlayed(response.data.tracks);
        } catch (error) {
            console.error('Error fetching listening history:', error);
            // Handle error if necessary
        }
    };

    // Fetch listening history when the component mounts
    useEffect(() => {
        const urlSearchParams = new URLSearchParams(location.search);
        const params = Object.fromEntries(urlSearchParams.entries());

        if (params.access_token && params.token_expiry) {
            // Store access token and its expiry time in local storage
            localStorage.setItem('spotify_access_token', params.access_token);
            localStorage.setItem('spotify_token_expiry', params.token_expiry);

            // Set the stored token in context
            setStoredToken(params.access_token);

            // Log the access token
        console.log('Access Token:', params.access_token);

            // Fetch listening history
            handleListeningHistory();
        }
    }, []); // Empty dependency array ensures the effect runs only once, on component mount

//     return (
//         <div>
//             <h1>Listening History</h1>
//             {/* Button to initiate Spotify login */}
//             <button onClick={handleSpotifyLogin}>Login with Spotify</button>
//               {/* Button to fetch listening history */}
//              <button onClick={handleListeningHistory}>Fetch Listening History</button>
//              {/* Button to fetch listening history */}
//             {recentlyPlayed.length > 0 &&
//                 <div>
//                     <h2>Recently Played Tracks</h2>
//                     <ul>
//                         {recentlyPlayed.map((track, index) => (
//                             <li key={index}>
//                                 <p>Track: {track.track_name}</p>
//                                 <p>Artist: {track.artist_name}</p>
//                                 <p>Album: {track.album_name}</p>
//                                 <p>Played At: {track.played_at}</p>
//                             </li>
//                         ))}
//                     </ul>
//                 </div>
//             }
//         </div>
//     );
// };

    return (
        <div className="listening-history-container">
            <h1>Listening History</h1>
            {/* Button to initiate Spotify login */}
             <button onClick={handleSpotifyLogin}>Login with Spotify</button>
            {/* Button to fetch listening history */}
            <button onClick={handleListeningHistory}>Fetch Listening History</button>

            {/* Render each track in its own individual bubble */}
            <div className="tracks-container">
                {recentlyPlayed.map((track, index) => (
                    <div key={index} className="track-bubble">
                        <p className="track-info">Track: {track.track_name}</p>
                        <p className="track-info">Artist: {track.artist_name}</p>
                        <p className="track-info">Album: {track.album_name}</p>
                        <p className="track-info">Played At: {track.played_at}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};


export default ListeningHistory;

