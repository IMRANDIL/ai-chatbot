const express = require('express');
const axios = require('axios');
const app = express();
const port = 4000;
const cors = require('cors')
app.use(express.json());
app.use(cors())


app.post('/chat', async (req, res) => {
    const { message } = req.body;

    try {
        const response = await axios.post('http://127.0.0.1:5000/process', {
            input: message
        });
        console.log('jsonResponse>>>>>>>>>>>>>>>>>>>>', response?.data)
        res.json({ response: response.data });
    } catch (error) {
        console.error("Error processing message", error);
        res.status(500).json({ error: "Error processing the message" });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
