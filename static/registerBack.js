document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.querySelector('.form-box-Register #registerForm'); // Select the register form within .form-box-Register
    const loginForm = document.querySelector('.form-box-Login #loginForm'); // Select the login form within .form-box-Login

    if (registerForm) {
        registerForm.addEventListener('submit', (event) => {
            event.preventDefault();

            // Get the input fields from the register form specifically
            const username = registerForm.querySelector('#username').value.trim();
            const password = registerForm.querySelector('#password').value.trim();
            const confirmPassword = registerForm.querySelector('#confirmpassword').value.trim();

            if (password !== confirmPassword) {
                alert("Passwords do not match!");
                return;
            }

            alert("Passwords match!");

            fetch("/Home/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(), // Get CSRF token
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                    confirmpassword: confirmPassword
                })
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.message) {
                        alert(data.message || "Registration successful!");
                        registerForm.reset();
                    } else {
                        alert(data.error || "An error occurred!");
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                    alert("An unexpected error occurred.");
                });
        });
    }

    // if (loginForm) {
    //     loginForm.addEventListener('submit', (event) => {
    //         event.preventDefault();

    //         // Get the input fields from the login form specifically
    //         const username = loginForm.querySelector('#username').value.trim();
    //         const password = loginForm.querySelector('#password').value.trim();

    //         fetch("/login/", {
    //             method: "POST",
    //             headers: {
    //                 "Content-Type": "application/json",
    //                 "X-CSRFToken": getCSRFToken(), // Get CSRF token
    //             },
    //             body: JSON.stringify({
    //                 username: username,
    //                 password: password
    //             })
    //         })
    //             .then((response) => response.json())
    //             .then((data) => {
    //                 if (data.message) {
    //                     alert(data.message || "Login successful!");
    //                     loginForm.reset();
    //                 } else {
    //                     alert(data.error || "Invalid login credentials!");
    //                 }
    //             })
    //             .catch((error) => {
    //                 console.error("Error:", error);
    //                 alert("An unexpected error occurred.");
    //             });
    //     });
    // }
});

function getCSRFToken() {
    const cookies = document.cookie.split(";");
    for (const cookie of cookies) {
        const [name, value] = cookie.trim().split("=");
        if (name === "csrftoken") {
            return value;
        }
    }
    return "";
}
