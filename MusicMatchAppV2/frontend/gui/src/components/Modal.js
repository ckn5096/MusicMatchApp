import React from 'react';

const Modal = ({ track, onClose }) => {
    if (!track) return null;

    const { name, artist, album_art_urls, spotify_link, artist_info } = track;

    return (
        <div className="modal-overlay">
            <div className="modal-content">
                <button onClick={onClose} className="close-button">Close</button>
                <h2>{name}</h2>
                <div className="album-art-container">
                    <img src={album_art_urls[2]} alt={`Album Art`} className="album-art-large" />
                </div>
                <p>Artist: {artist}</p>
                <p>{artist_info}</p>
                <a href={spotify_link} target="_blank" rel="noopener noreferrer">Listen on Spotify</a>
            </div>
        </div>
    );
};

export default Modal;
