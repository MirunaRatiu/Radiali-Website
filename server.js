const express = require('express');
const mysql = require('mysql');
const cors = require('cors');
const app = express();
const port = 3306;

app.use(cors());
app.use(express.json()); // Pentru a putea prelucra datele JSON

// Configurare conexiune la baza de date MySQL
const db = mysql.createConnection({
        database: 'radialidb',      
        user: 'root',         
        password: 'Mysql1234',           
        host: '127.0.0.1',                  
                 // numele bazei de date
});

// Conectare la baza de date
db.connect((err) => {
  if (err) {
    console.error('Eroare la conexiunea cu baza de date:', err);
    return;
  }
  console.log('Conectat la baza de date MySQL');
});

// Endpoint pentru adăugarea unei categorii
app.post('/api/addCategory', (req, res) => {
  const { name, image_url, slug, description } = req.body;

  const query = 'INSERT INTO categories (name, image_url, slug, description) VALUES (?, ?, ?, ?)';
  db.query(query, [name, image_url, slug, description], (err, result) => {
    if (err) {
      return res.status(500).json({ error: 'Eroare la adăugarea categoriei' });
    }
    res.status(200).json({ message: 'Categorie adăugată cu succes' });
  });
});

// Endpoint pentru obținerea categoriilor
app.get('/api/getCategories', (req, res) => {
  const query = 'SELECT * FROM categories';
  db.query(query, (err, result) => {
    if (err) {
      return res.status(500).json({ error: 'Eroare la obținerea categoriilor' });
    }
    res.status(200).json(result);
  });
});

// Pornire server
app.listen(port, () => {
  console.log(`Serverul rulează pe http://localhost:${port}`);
});
