// //AuthContext.js
// import { createContext, useContext, useState } from 'react';
//
// const AuthContext = createContext();
//
// const AuthProvider = ({ children }) => {
//     const [authToken, setAuthToken] = useState(null);
//
//     const login = (token) => {
//         setAuthToken(token);
//     };
//
//     const logout = () => {
//         setAuthToken(null);
//     };
//
//     return (
//         <AuthContext.Provider value={{ authToken, login, logout }}>
//             {children}
//         </AuthContext.Provider>
//     );
// };
//
//
// const useAuth = () => {
//     return useContext(AuthContext);
// };
//
// export { AuthProvider, useAuth };


// AuthContext.js
import { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
    const [authToken, setAuthToken] = useState(null);

    // Update localStorage or sessionStorage when authToken changes
    useEffect(() => {
        if (authToken) {
            localStorage.setItem('authToken', authToken);
            // Alternatively, you can use sessionStorage for temporary storage
            // sessionStorage.setItem('authToken', authToken);


        } else {
           // localStorage.removeItem('authToken');
            // sessionStorage.removeItem('authToken');
        }

    }, [authToken]);

        // Load token from localStorage or sessionStorage on component mount
    useEffect(() => {
        const storedToken = localStorage.getItem('authToken') || sessionStorage.getItem('authToken');
        console.log('Stored Token:', storedToken); // Add this line
        if (storedToken) {
            setAuthToken(storedToken);
        }
    }, []);

    const login = (token) => {
        setAuthToken(token);

    };

    const logout = () => {
        setAuthToken(null);
        localStorage.removeItem('authToken');
    };

<<<<<<< HEAD

    return (
        <AuthContext.Provider value={{ authToken, login, logout }}>
=======
    // Add setStoredToken here
    const setStoredToken = (token) => {
        setAuthToken(token);
    };


    return (
        <AuthContext.Provider value={{ authToken, login, logout , setStoredToken }}>
>>>>>>> origin/master
            {children}
        </AuthContext.Provider>
    );
};

// const useAuth = () => {
//     return useContext(AuthContext);
// };

const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return { ...context, storedToken: localStorage.getItem('authToken') || sessionStorage.getItem('authToken') };
};

export { AuthProvider, useAuth  };
