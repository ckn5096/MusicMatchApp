/*
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
*/
// index.js or your main entry point
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import App from './App';
import Registration from "./components/Registration";
import Login from "./components/Login";
import Home from "./components/Home";
import { AuthProvider } from './components/AuthContext';
import ProfileUpdate from "./components/ProfileUpdate";
import MusicPreference from "./components/MusicPreference";
<<<<<<< HEAD
=======
import ListeningHistory from "./components/ListeningHistory";
>>>>>>> origin/master

ReactDOM.render(
  <React.StrictMode>
    <Router>
        <AuthProvider>
      <Routes>
          <Route path="/" element={<App />} />
        <Route path="/Registration" element={<Registration />} />
           <Route path="/Login" element={<Login />} />
          <Route path="/home" element={<Home />} />
          <Route path="/profile/update" element={ <ProfileUpdate />} />
          <Route path="/MusicPreference" element={ <MusicPreference />} />
<<<<<<< HEAD
=======
           <Route path="/ListeningHistory" element={ <ListeningHistory />} />
>>>>>>> origin/master
      </Routes>
        </AuthProvider>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);

