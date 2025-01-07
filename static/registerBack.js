document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById("registerForm");

    if (registerForm) {
        registerForm.addEventListener('submit', (event) => {
            event.preventDefault();

            const username = document.getElementById("username").value.trim();
            const password = document.getElementById("password").value.trim();
            const confirmPassword = document.getElementById("confirmpassword").value.trim();

            if (password !== confirmPassword) {
                alert("Passwords do not match!");
                return;
            }

            if (password === confirmPassword) {
                alert("Passwords match!");
            }

            fetch("/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(), // Get CSRF token
                },
                body: JSON.stringify({
                    username: username,
                    password: password
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
