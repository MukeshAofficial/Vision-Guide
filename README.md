# Vision Guide

The Vision Guide is a revolutionary project aimed at providing assistance through voice commands, with a primary focus on aiding users in obtaining information and recognizing objects through images.

## Features

### Voice-Based Question Answering
- Users can initiate conversations by speaking commands such as "Go to GPT".
- Voice input is converted to text using a speech-to-text module.
- The text is passed to Gemini, our question-answering system.
- Gemini processes the query and generates a response.
- The response is converted back to speech using a text-to-speech module and communicated to the user.

### Image Recognition
- Users can activate image recognition by speaking commands like "Scan photo".
- The camera module opens to capture an image when prompted by the user.
- The captured image is analyzed by Gemini for recognition.
- Gemini generates a simple description of the image's content.
- The description is converted to speech and communicated to the user.

## Technologies Used
- Speech-to-text module for converting voice input to text.
- Text-to-speech module for converting responses to speech.
- Gemini for question answering and image recognition.
- Camera module for capturing images.

## Usage
1. Clone the repository.
2. Install the necessary dependencies.
3. Run the main application.
4. Use voice commands to interact with the system.
