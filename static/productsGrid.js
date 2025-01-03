// Define the prototype object for a product
const CategoryPrototype = {
    name: '',
    image_url: '',
    slug: '',
    description: '',
    create() {
        const gridItem = document.createElement('a');
        gridItem.href = this.slug;
        gridItem.classList.add('grid-item');

        const nameElement = document.createElement('p');
        nameElement.classList.add('grid-item-name');
        nameElement.textContent = this.name;

        const imgElement = document.createElement('img');
        imgElement.src = this.image_url;
        imgElement.alt = this.name;
        imgElement.loading = 'lazy';

        gridItem.appendChild(nameElement);
        gridItem.appendChild(imgElement);

        const descriptionElement = document.createElement('p');
        descriptionElement.classList.add('grid-item-description');
        descriptionElement.textContent = this.description;
        gridItem.appendChild(descriptionElement);

        return gridItem;
    }
};

// Preluare categoriilor din baza de date
document.addEventListener('DOMContentLoaded', () => {
    fetch('http://127.0.0.1:8000/api/getCategories')
        .then(response => response.json())
        .then(categories => {
            const grid = document.getElementById('categoryGrid');
            categories.forEach(categoryData => {
                const category = Object.create(CategoryPrototype);
                category.name = categoryData.name;
                category.slug = categoryData.slug;
                category.image_url = categoryData.image_url;
                category.description = categoryData.description;

                const gridItem = category.create();
                grid.appendChild(gridItem);
            });
        })
        .catch(error => console.error('Eroare:', error));
});
