document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.querySelector('.form-box-Login form'); // Select the login form
    const usernameInput = document.getElementById('username'); // Username input field
    const passwordInput = document.getElementById('password'); // Password input field

    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent default form submission

            const username = usernameInput.value.trim();
            const password = passwordInput.value.trim();

            // Ensure fields are not empty
            if (!username || !password) {
                alert("Please enter both username and password!");
                return;
            }

            // Send AJAX POST request to Django endpoint for login
            fetch('/api/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(), // Retrieve CSRF token
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                }),
            })
                .then((response) => {
                    if (response.ok) {
                        alert("Login successful!");
                        window.location.href = '/dashboard/'; // Redirect to the dashboard or desired page
                    } else {
                        return response.json().then((data) => {
                            alert(data.error || "Invalid login credentials!");
                        });
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                    alert("An error occurred while logging in.");
                });
        });
    }
});
