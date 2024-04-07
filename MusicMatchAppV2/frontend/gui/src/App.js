// import React from 'react';
// import { Link } from 'react-router-dom';
// import logo from './logo.png';
// import './App.css';
//
// function App() {
//   return (
//     <div className="container">
//       <img src={logo} className="logo" alt="logo" />
//       <h1>Welcome to Music Match</h1>
//          <p>Discover and enjoy your favorite music </p>
//          <p>Register now to create playlists, explore music preferences, and more </p>
//       <Link to="/Registration" className="link">
//         <button className="link-button">Sign Up</button>
//       </Link>
//       <Link to="/Login" className="link">
//         <button className="link-button">Login</button>
//       </Link>
//     </div>
//   );
// }
//
// export default App;


import React, {useEffect, useState} from 'react';
import { Link } from 'react-router-dom';
import logo from './logo.png';
import './App.css';
import soundFile from './sound.mp3'; // Import the sound file
import backgroundSound from './backgroundSound.mp3'; // Import the sound file

function App() {
  const [isRotating, setIsRotating] = useState(true); // State variable to control rotation

  const toggleRotation = () => {
    setIsRotating(!isRotating); // Toggle rotation state
  };

  const playSound = () => {
    const audio = new Audio(soundFile);
    audio.play(); // Play the sound
  };

  useEffect(() => {
    const audio = new Audio(backgroundSound);
    audio.loop = true; // Loop the background sound
      audio.play(); // Start playing the background sound
    return () => {
      audio.pause(); // Pause the background sound when component unmounts
    };
  }, []); // Run this effect only once when component mounts

 useEffect(() => {
    // Function to create and animate music notes
    const createMusicNote = () => {
      const noteTypes = ['music-note1', 'music-note2', 'music-note3','music-note4']; // List of different music note types
      const container = document.getElementById('music-notes-container');
      const noteType = noteTypes[Math.floor(Math.random() * noteTypes.length)]; // Randomly choose a note type
      const note = document.createElement('div');
      note.className = `music-note ${noteType}`;

       // Generate random scale factor between 0.5 and 1.5
      const scaleFactor = Math.random() * 2.5; // Adjust range as needed

      // Apply random scale transformation to the note
      note.style.transform = `scale(${scaleFactor})`;

      container.appendChild(note);

      const startX = Math.random() * window.innerWidth; // Random X position within the window width
      const endX = Math.random() * window.innerWidth; // Random X position for animation end point
      const duration = Math.random() * 5000 + 3000; // Random duration between 3 to 8 seconds

      note.style.left = `${startX}px`; // Set initial X position
      note.style.animation = `fall ${duration}ms linear forwards`; // Start falling animation

      // Remove the note when animation ends
      note.addEventListener('animationend', () => {
        note.remove();
      });
    };

    // Call createMusicNote function at intervals to create music notes continuously
    const intervalId = setInterval(createMusicNote, 1000);

    // Clear the interval when component unmounts to stop creating music notes
    return () => {
      clearInterval(intervalId);
    };
  }, []); // Run this effect only once when component mounts

  return (
    <div className="container">

        {/* Container to hold the falling music notes */}
      <div id="music-notes-container"></div>

      <img
        src={logo}
        className={isRotating ? 'logo rotating' : 'logo'}
        alt="logo"
        onClick={() => { toggleRotation(); playSound(); }} // Toggle rotation and play sound on click
      />


<<<<<<< HEAD
      <h1>Welcome to Music Match</h1>
=======
      <h1>Welcome to MelodyMatch</h1>
>>>>>>> origin/master
      <p>Discover and enjoy your favorite music</p>
      <p>Register now to create playlists, explore music preferences, and more</p>
      <Link to="/Registration" className="link">
        <button className="link-button">Sign Up</button>
      </Link>
      <Link to="/Login" className="link">
        <button className="link-button">Login</button>
      </Link>
    </div>
  );
}

export default App;
