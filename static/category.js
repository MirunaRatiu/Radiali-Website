// Define a prototype-based class for "TabelaCategorie"
function TabelaCategorie(id, denumire, poza, linkPaginaProduse) {
    this.id = id;
    this.denumire = denumire;
    this.poza = poza;
    this.linkPaginaProduse = linkPaginaProduse;
}

// Method to display category details
TabelaCategorie.prototype.displayDetails = function() {
    console.log(`ID: ${this.id}`);
    console.log(`Denumire: ${this.denumire}`);
    console.log(`Poza: ${this.poza}`);
    console.log(`Link către pagina produse: ${this.linkPaginaProduse}`);
};

// Function to integrate the class with HTML content
function renderCategorieInHTML(categorie) {
    const container = document.getElementById('categorii-container');

    // Create a category card
    const card = document.createElement('div');
    card.className = 'categorie-card';

    // Add image
    const img = document.createElement('img');
    img.src = categorie.poza;
    img.alt = categorie.denumire;
    card.appendChild(img);

    // Add title
    const title = document.createElement('h3');
    title.textContent = categorie.denumire;
    card.appendChild(title);

    // Add link
    const link = document.createElement('a');
    link.href = categorie.linkPaginaProduse;
    link.textContent = 'Vezi Produse';
    card.appendChild(link);

    // Append card to container
    container.appendChild(card);
}

// Array of categories
const categorii = [
    new TabelaCategorie(1, 'Generatoare', 'https://i.postimg.cc/tRSBZ9dR/eu30-removebg-preview.png', '/produse/generatoare'),
    new TabelaCategorie(2, 'Mai Compactor', 'https://ntc.cz/thumbcache/k5qaw0qw051g8wo2au9jtwmswl1eaqkh1flnhan3qqu31w2ot9s5slu-wjgmszxakwwyjtl3251fqj5i5dlagx-zltt0bjgzrflesdie.png', '/produse/mai-compactor'),
    new TabelaCategorie(3, 'Placi Compactoare', 'https://ntc.cz/thumbcache/k5qaw0qw051g8wo2au9jtwmswl1eaqkh1flnhan3qmqs2oexhvpjnvkpfoq3qatat1ifn79qwwzp51pi5mxvmiqjt0dfmuna0fyuiafv8.png', '/produse/placi-compactoare'),
    new TabelaCategorie(4, 'Taietor Beton', 'poza-electronice.jpg', '/produse/taietor-beton'),
    new TabelaCategorie(5, 'Motoare Honda', 'https://i.postimg.cc/Kj6LPpvf/wh20-removebg-preview.png', '/produse/motoare-honda'),
    new TabelaCategorie(6, 'Motopompe de apa', 'https://i.postimg.cc/Kj6LPpvf/wh20-removebg-preview.png', '/produse/motopompe-de-apa'),
    new TabelaCategorie(7, 'Ciocane Hidraulice', 'https://i.postimg.cc/k4ZtCY8C/R-removebg-preview.png4', '/produse/ciocane-hidraulice'),
    new TabelaCategorie(8, 'Piese Miniexcavator', 'https://i.postimg.cc/c1rj0F2b/14559741-piese-motor-perkins-jcb-catbobcat-miniexcavator-1-removebg-preview.png', '/produse/piese-miniexcavator'),
    new TabelaCategorie(9, 'Cilindru Compactor', 'https://i.postimg.cc/CKhPt7bJ/k5qaw0qw051g8wo2au9jtwmswl1eaqkh1flnhan3orocd7gkj13oego0ec2mpifgbj6ubkfzhbhxxblga-removebg-preview.png', '/produse/cilindru-compactor')
];

// Render all categories
categorii.forEach(categorie => {
    categorie.displayDetails();
    renderCategorieInHTML(categorie);
});
