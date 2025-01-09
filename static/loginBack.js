// document.addEventListener('DOMContentLoaded', () => {
//     const loginForm = document.querySelector('#loginForm'); // Select the login form

//     if (loginForm) {
//         loginForm.addEventListener('submit', (event) => {
//             event.preventDefault(); // Prevent default form submission

//             // Select the username and password input fields within the login form
//             const usernameInput = loginForm.querySelector('#username');
//             const passwordInput = loginForm.querySelector('#password');

//             const username = usernameInput.value.trim();
//             const password = passwordInput.value.trim();

//             // Ensure fields are not empty
//             if (!username || !password) {
//                 alert("Please enter both username and password!");
//                 return;
//             }

//             // Send AJAX POST request to Django endpoint for login
//             fetch('/Home/login/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': getCSRFToken(), // Retrieve CSRF token
//                 },
//                 body: JSON.stringify({
//                     username: username,
//                     password: password,
//                 }),
//             })
//                 .then((response) => {
//                     if (response.ok) {
//                         alert("Login successful!");
//                         loginContainer.style.display = 'none';


//                     } else {
//                         return response.json().then((data) => {
//                             alert(data.error || "Invalid login credentials!");
//                         });
//                     }
//                 })
//                 .catch((error) => {
//                     console.error("Error:", error);
//                     alert("An error occurred while logging in.");
//                 });
//         });
//     }
// });

// function getCSRFToken() {
//     const cookies = document.cookie.split(";");
//     for (const cookie of cookies) {
//         const [name, value] = cookie.trim().split("=");
//         if (name === "csrftoken") {
//             return value;
//         }
//     }
//     return "";
// }

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.querySelector('#loginForm'); // Selector corect pentru formular
    const loginContainer = document.querySelector('.loginContainer'); // Popup-ul de login
    const cartIcon = document.querySelector('.cart-icon'); // Iconița coșului de cumpărături
    const regLink = document.querySelector('.reg'); // Link-ul "Intra in cont"
    const logoutLink = document.querySelector('.logout'); // Logout link

    // Verifică dacă utilizatorul este logat
    const username = localStorage.getItem('username');
    if (username) {
        cartIcon.style.display = 'block'; // Afișează coșul de cumpărături
        regLink.style.display = 'none'; // Ascunde link-ul "Intra in cont"
        logoutLink.style.display = 'block'; // Afișează logout
    }

    // Gestionare login
    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Previne trimiterea implicită a formularului

            const usernameInput = loginForm.querySelector('#username');
            const passwordInput = loginForm.querySelector('#password');

            const username = usernameInput.value.trim();
            const password = passwordInput.value.trim();

            if (!username || !password) {
                alert("Please enter both username and password!");
                return;
            }

            fetch('/Home/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                }),
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.message) {
                        alert("Login successful!");

                        // Închide popup-ul
                        loginContainer.style.display = 'none';

                        // Arată coșul de cumpărături
                        cartIcon.style.display = 'block';

                        // Ascunde link-ul "Intra in cont" și arată logout
                        regLink.style.display = 'none';
                        logoutLink.style.display = 'block';

                        // Setează username-ul local
                        localStorage.setItem('username', username);
                    } else {
                        alert(data.error || "Invalid login credentials!");
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                    alert("An error occurred while logging in.");
                });
        });
    }

    // Gestionare logout
    if (logoutLink) {
        logoutLink.addEventListener('click', (e) => {
            e.preventDefault();

            fetch('/logout/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCSRFToken(),
                },
            })
                .then(() => {
                    alert("Logged out successfully!");

                    // Resetare vizualizare
                    cartIcon.style.display = 'none';
                    regLink.style.display = 'block';
                    logoutLink.style.display = 'none';

                    // Șterge username-ul din localStorage
                    localStorage.removeItem('username');
                })
                .catch((error) => {
                    console.error("Error:", error);
                });
        });
    }
});

function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return '';
}
