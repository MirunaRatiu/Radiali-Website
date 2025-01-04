document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.loginContainer');
    const LoginLink = document.querySelector('.SignInLink');
    const RegisterLink = document.querySelector('.SignUpLink');
    const inchidPop = document.querySelector('.closeBtn');
    const showPop = document.querySelector('.reg');

    //container.classList.add('rem');

    if(showPop){
        showPop.addEventListener('click', () => {
            container.classList.add('act');
            container.classList.remove('rem');
        });
    }

    if(inchidPop){
        inchidPop.addEventListener('click', () => {
            container.classList.add('rem');
            container.classList.remove('act');
        });
    }

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
// }

