const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(express.json());

app.use(express.static(path.join(__dirname, 'public')));

const DATA_FILE = 'user_interaction_log.csv';

if (!fs.existsSync(DATA_FILE)) {
    fs.writeFileSync(DATA_FILE, 'timestamp,mouseMovements,avgTypingSpeed,clicks,keypresses,Result\n');
}

app.post('/collect', (req, res) => {
    const data = req.body;
    const timestamp = new Date().toISOString();
    const line = `${timestamp},${data.mouseMovements},${data.avgTypingSpeed},${data.clicks},${data.keypresses},Human\n`;
    fs.appendFile(DATA_FILE, line, (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            res.status(500).json({ status: 'error' });
        } else {
            console.log('Data saved:', data);
            res.json({ status: 'success' });
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
