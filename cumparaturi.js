document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent any default button behavior
            const productName = this.dataset.productName;
            console.log('Adding product to cart:', productName);
            
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
                    alert(`Product "${productName}" added to cart successfully!`);
                    // Update stock display if you have a stock element
                    const stockElement = document.querySelector(`[data-stock="${productName}"]`);
                    if (stockElement) {
                        stockElement.textContent = data.new_stock;
                    }
                } else {
                    alert(data.error || 'Failed to add product to cart');
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
