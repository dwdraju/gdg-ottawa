const express = require('express');
const path = require('path');
const compression = require('compression');
const morgan = require('morgan');

const app = express();
const PORT = process.env.PORT || 8080;

// Middleware
app.use(compression());
app.use(morgan('dev'));

// Serve static files from current directory (where index.html lives)
const publicDir = path.join(__dirname);
app.use(express.static(publicDir, { maxAge: '1h' }));

// Fallback to index.html for SPA-style navigation
app.get('/', (req, res) => {
  res.sendFile(path.join(publicDir, 'index.html'));
});

// 404 for other missing assets
app.use((req, res) => {
  res.status(404).send('Not found');
});

app.listen(PORT, () => {
  console.log(`DevFest Ottawa site running at http://localhost:${PORT}`);
});
