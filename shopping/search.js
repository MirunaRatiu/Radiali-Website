document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('input[name="q"]');
    const suggestionsList = document.createElement('ul');
    suggestionsList.className = 'suggestions-list';
    searchInput.parentNode.appendChild(suggestionsList);

    searchInput.addEventListener('input', function() {
        const query = this.value;
        if (query.length > 2) {
            fetch(`/productManagement/search-suggestions/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsList.innerHTML = '';
                    data.suggestions.forEach(suggestion => {
                        const li = document.createElement('li');
                        li.textContent = suggestion;
                        li.addEventListener('click', () => {
                            searchInput.value = suggestion;
                            suggestionsList.innerHTML = '';
                        });
                        suggestionsList.appendChild(li);
                    });
                });
        } else {
            suggestionsList.innerHTML = '';
        }
    });
});
