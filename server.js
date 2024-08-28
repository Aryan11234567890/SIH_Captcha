const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Serve the HTML file
app.use(express.static(path.join(__dirname, 'public')));

// Define the CSV file to store data
const DATA_FILE = 'user_interaction_log.csv';

// Create CSV file with headers if it doesn't exist
if (!fs.existsSync(DATA_FILE)) {
    fs.writeFileSync(DATA_FILE, 'timestamp,mouseMovements,avgTypingSpeed,clicks,keypresses\n');
}

// Endpoint to receive and store data
app.post('/collect', (req, res) => {
    const data = req.body;

    // Add a timestamp to the data
    const timestamp = new Date().toISOString();

    // Save data to the CSV file
    const line = `${timestamp},${data.mouseMovements},${data.avgTypingSpeed},${data.clicks},${data.keypresses}\n`;
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

// Start the server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
