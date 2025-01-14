document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productName = this.dataset.productName;
            console.log('Button clicked for product:', productName); // Debug log
            
            // Show immediate feedback
            alert('Clicked! Adding product to cart...');
            
            fetch('/shopping/sync-cart/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken(),
                },
                body: JSON.stringify({
                    product_name: productName,
                    action: 'add'
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Product successfully added to cart!');
                } else {
                    alert('Could not add product to cart: ' + data.error);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error adding product to cart');
            });
        });
    });
});
function getCsrfToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}
<button class="add-to-cart-btn" data-product-name="{{ product.name }}">Add to Cart</button>
