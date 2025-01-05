document.addEventListener('DOMContentLoaded', function () {
    const modals = document.querySelectorAll('.modal');
    
    modals.forEach((modal) => {
        modal.addEventListener('shown.bs.modal', () => {
            console.log('Modalul a fost deschis');
        });
        
        modal.addEventListener('hidden.bs.modal', () => {
            console.log('Modalul a fost închis');
        });
    });
});
