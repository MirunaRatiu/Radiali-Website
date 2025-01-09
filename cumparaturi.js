document.addEventListener('DOMContentLoaded', function () {
    const cartCountElement = document.querySelector('.cart-count');
    const addToCartButtons = document.querySelectorAll('.add-to-cart');

    // Funcție pentru actualizarea coșului
    function updateCart(productId, action) {
        console.log(`Updating cart: Product ID = ${productId}, Action = ${action}`); // Log pentru depanare
    
        fetch('/shopping/sync-cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({ product_id: productId, action: action })
        })
            .then(response => response.json())
            .then(data => {
                console.log('Response from server:', data); // Log pentru răspunsul serverului
                if (data.cart_count !== undefined) {
                    cartCountElement.textContent = data.cart_count;
                }
            })
            .catch(error => {
                console.error('Eroare la sincronizarea coșului:', error);
            });
    }
    

    addToCartButtons.forEach(button => {
        const productId = button.dataset.productId;

        button.addEventListener('click', function () {
            const action = button.classList.contains('btn-danger') ? 'remove' : 'add';

            // Actualizăm coșul prin backend
            updateCart(productId, action);

            // Schimbăm textul și stilul butonului
            if (action === 'add') {
                button.textContent = 'Elimină din coș';
                button.classList.remove('btn-primary');
                button.classList.add('btn-danger');
            } else {
                button.textContent = 'Adaugă în coș';
                button.classList.remove('btn-danger');
                button.classList.add('btn-primary');
            }
        });
    });

    // Funcție pentru obținerea token-ului CSRF
    function getCSRFToken() {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith('csrftoken=')) {
                return cookie.substring('csrftoken='.length);
            }
        }
        return '';
    }
});
