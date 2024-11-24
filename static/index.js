document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.loginContainer');
    const LoginLink = document.querySelector('.SignInLink');
    const RegisterLink = document.querySelector('.SignUpLink');

    if (RegisterLink) {
        RegisterLink.addEventListener('click', () => {
            container.classList.add('active');
        });
    }

    if (LoginLink) {
        LoginLink.addEventListener('click', () => {
            container.classList.remove('active');
        });
    }
});

// const modal = document.querySelector('.loginContainer');
// const openModal = document.querySelector('#reg');
// const closeModal = document.querySelector('.closeBtn');

// openModal.addEventListener('click', () => {
//     modal.showModal();
// })


// Select all hyperlinks with id="reg"
//Add click event listeners to all #reg links
document.querySelectorAll("#reg").forEach(function (link) {
    link.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent hyperlink navigation
        document.querySelector(".loginContainer").classList.add("act");
    });
});

// // Close modal when close button is clicked
document.querySelector(".loginContainer .closeBtn").addEventListener("click", function () {
    document.querySelector(".loginContainer").classList.remove("act");
});

