const express = require('express');
const multer = require('multer');
const path = require('path');

const body_parser = require('body-parser');
const { spawn } = require('child_process');
const { log } = require('console');
const app = express();
const PORT = process.env.PORT || 3000;

// Multer for file upload
const upload = multer({ dest: 'uploads/' });

app.use(body_parser.urlencoded({ extended: true }));
// Serve index.html
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// Handle file upload
app.post('/upload', upload.single('video'), (req, res) => {
    if (!req.file) {
        return res.status(400).send('No file uploaded.');
    }
    const language = req.body.languages;
    // Access the uploaded file path
    const filePath = req.file.path;
    // Call Python script and pass the file path as an argument
    // const output_path = 'C:/Users/skfog/OneDrive/Desktop/project/site/output/audio.wav'
    const pythonProcess = spawn('python', ['C:/Users/skfog/OneDrive/Desktop/project/backend/master.py', filePath, language]);

    // Handle stdout, stderr, and process events as needed
    pythonProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        // Handle process completion, if needed
    });

    // Send a response indicating that the file has been passed to the Python script
    // res.send('File passed to Python script for processing.');
    res.sendFile(__dirname + '/out.html')
});
app.get('/translated-video', (req, res) => {
    // Assuming translated video files are stored in a directory named 'translated-videos'
    const videoPath = 'C:/Users/skfog/OneDrive/Desktop/project/site/output_video.mp4';

    // Send the video file as a response
    res.sendFile(videoPath);
});


// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

