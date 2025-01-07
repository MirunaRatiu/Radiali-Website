document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.loginContainer');
    const LoginLink = document.querySelector('.SignInLink');
    const RegisterLink = document.querySelector('.SignUpLink');
    const inchidPop = document.querySelector('.closeBtn');
    const showPop = document.querySelector('.reg');


    const isHomePage = window.location.pathname === '/Home/home/';

    if (!isHomePage) {
        if (showPop) {
            showPop.addEventListener('click', () => {
                container.classList.add('act');
                container.classList.remove('rem');
            });
        }
    }
     if (isHomePage) {
         if (inchidPop) {
             inchidPop.addEventListener('click', () => {
                 container.classList.add('rem');
                 container.classList.remove('act');
             });
         }
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
