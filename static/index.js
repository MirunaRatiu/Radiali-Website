// document.addEventListener('DOMContentLoaded', () => {
//     const container = document.querySelector('.loginContainer');
//     const LoginLink = document.querySelector('.SignInLink');
//     const RegisterLink = document.querySelector('.SignUpLink');
//     const inchidPop = document.querySelector('.closeBtn');
//     const showPop = document.querySelector('.reg');

//     //container.classList.add('rem');

//     if(showPop){
//         showPop.addEventListener('click', () => {
//             container.classList.add('act');
//             container.classList.remove('rem');
//         });
//     }

//     if(inchidPop){
//         inchidPop.addEventListener('click', () => {
//             container.classList.add('rem');
//             container.classList.remove('act');
//         });
//     }

//     if (RegisterLink) {
//         RegisterLink.addEventListener('click', () => {
//             container.classList.add('active');
//         });
//     }

//     if (LoginLink) {
//         LoginLink.addEventListener('click', () => {
//             container.classList.remove('active');
//         });
//     }
// });

// document.addEventListener('DOMContentLoaded', () => {
//     const container = document.querySelector('.loginContainer');
//     const LoginLink = document.querySelector('.SignInLink');
//     const RegisterLink = document.querySelector('.reg'); // Asigură-te că ID-ul este corect
//     const inchidPop = document.querySelector('.closeBtn');
//     const showPop = document.querySelector('.reg');

//     // Când utilizatorul apasă pe butonul "Intra în cont"
//     if (showPop) {
//         showPop.addEventListener('click', (event) => {
//             event.preventDefault(); // Previi comportamentul implicit al link-ului
//             container.classList.add('act'); // Adaugă clasa care face vizibil pop-up-ul
//         });
//     }

//     // Când utilizatorul apasă pe "Inregistreaza-te"
//     if (RegisterLink) {
//         RegisterLink.addEventListener('click', (event) => {
//             event.preventDefault(); // Previi comportamentul implicit al link-ului
//             container.classList.add('act'); // Adaugă clasa care face vizibil pop-up-ul
//         });
//     }

//     // Când utilizatorul apasă pe "X" (butonul de închidere)
//     if (inchidPop) {
//         inchidPop.addEventListener('click', (event) => {
//             event.preventDefault(); // Previi comportamentul implicit (dacă este cazul)
//             container.classList.remove('act'); // Elimină clasa care face pop-up-ul vizibil
//         });
//     }

//     // Funcționalități adiționale pentru RegisterLink și LoginLink (schimbare între Login/Register)
//     if (LoginLink) {
//         LoginLink.addEventListener('click', (event) => {
//             container.classList.remove('act'); // Înlătură starea "active" pentru login
//         });
//     }

    
// });




document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.loginContainer');
    const LoginLink = document.querySelector('.SignInLink'); // Link-ul pentru Login
    const RegisterLink = document.querySelector('.SignUpLink'); // Link-ul pentru Register
    const inchidPop = document.querySelector('.closeBtn');
    const showPop = document.querySelector('.reg'); // Butonul care deschide pop-up-ul

    // Când utilizatorul apasă pe butonul "Intra în cont"
    if (showPop) {
        showPop.addEventListener('click', (event) => {
            event.preventDefault(); // Previi comportamentul implicit al link-ului
            container.classList.add('act'); // Adaugă clasa care face vizibil pop-up-ul
        });
    }

    // Când utilizatorul apasă pe "Inregistreaza-te"
    if (RegisterLink) {
        RegisterLink.addEventListener('click', (event) => {
            event.preventDefault(); // Previi comportamentul implicit al link-ului
            container.classList.add('active'); // Adaugă clasa care schimbă în formularul Register
        });
    }

    // Când utilizatorul apasă pe "X" (butonul de închidere)
    if (inchidPop) {
        inchidPop.addEventListener('click', (event) => {
            event.preventDefault(); // Previi comportamentul implicit (dacă este cazul)
            container.classList.remove('act'); // Elimină clasa care face pop-up-ul vizibil
        });
    }

    // Funcționalități adiționale pentru LoginLink (schimbare între Register/Login)
    if (LoginLink) {
        LoginLink.addEventListener('click', (event) => {
            event.preventDefault(); // Previi comportamentul implicit
            container.classList.remove('active'); // Înlătură starea "active" pentru Register
        });
    }
});
