# GPT-4-VOICE-ASSITANT
AI-Powered Voice Assistant

Overview

This AI-powered voice assistant integrates OpenAI's GPT-4 API with speech-to-text (Whisper) and text-to-speech (gTTS) to enable natural language conversations. It can execute system commands, provide real-time information, and respond to contextual queries.

Features

Speech Recognition: Uses OpenAI's Whisper to convert spoken input into text.

AI Response: Utilizes OpenAI's GPT-4 to generate responses.

Text-to-Speech: Converts AI responses to speech using gTTS.

Command Execution: Can perform system operations like opening applications.

Real-Time Information: Fetches live data (e.g., weather, news) based on queries.

Installation

Prerequisites

Ensure you have Python 3.8+ installed.

Install Dependencies

pip install openai speechrecognition gtts playsound pyaudio

For Linux, install additional dependencies:

sudo apt-get install portaudio19-dev
pip install pyaudio

Usage

Set Up OpenAI API Key

Obtain an API key from OpenAI and set it in an environment variable:

export OPENAI_API_KEY="your-api-key"

Or add it directly in the script:

openai.api_key = "your-api-key"

Run the Assistant

Execute the main script:

python main.py

How It Works

The assistant listens to user input via the microphone.

Converts speech to text using Whisper.

Sends the text to OpenAI's GPT-4 for a response.

Converts the response back to speech using gTTS.

Plays the generated audio response.

Customization

Modify the command execution feature to add more system operations.

Integrate weather APIs or other services for enhanced real-time responses.

Improve natural language understanding by fine-tuning prompt engineering.

Troubleshooting

No module named 'speech_recognition': Ensure dependencies are installed using pip install speechrecognition.

Error with PyAudio: On Linux, install portaudio19-dev before installing PyAudio.

Slow response time: Reduce the GPT-4 model's response length or optimize API calls.

License

This project is open-source under the MIT License.

Author

Developed by Dheeravath Bhagavan.

