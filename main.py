import openai
import speech_recognition as sr
import pyttsx3
import os
import keyboard
import requests
import wikipedia
import datetime
import random
from gtts import gTTS
import playsound
import tempfile

# Set up OpenAI API key
openai.api_key = "your-openai-api-key"

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speaking speed

def speak(text, use_pyttsx3=True):
    """Convert text to speech using pyttsx3 or gTTS."""
    if use_pyttsx3:
        engine.say(text)
        engine.runAndWait()
    else:
        try:
            tts = gTTS(text=text, lang="en")
            with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
                file_path = fp.name
                tts.save(file_path)
                playsound.playsound(file_path)
        except Exception as e:
            print(f"Error in text-to-speech: {e}")

def listen():
    """Capture audio and convert to text using SpeechRecognition"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio).lower()
        print(f"You: {text}")

        if "stop" in text or "exit" in text:
            speak("Goodbye! Have a great day!", use_pyttsx3=True)
            exit(0)

        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return ""
    except sr.RequestError:
        print("Speech service is down.")
        return ""

def gpt4_response(prompt):
    """Send a prompt to GPT-4 and get a response"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def get_time():
    """Fetch and return the current time."""
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    """Fetch and return the current date."""
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")


def search_wikipedia(query):
    """Fetch a summary from Wikipedia."""
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found."

def tell_joke():
    """Return a random joke."""
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ]
    return random.choice(jokes)

def execute_command(command):
    """Execute basic system commands like opening apps"""
    if "open notepad" in command:
        os.system("notepad.exe")
        return "Opening Notepad."
    elif "open calculator" in command:
        os.system("calc.exe")
        return "Opening Calculator."
    elif "open browser" in command:
        os.system("start chrome")
        return "Opening Browser."
    elif "shutdown" in command:
        os.system("shutdown /s /t 5")
        return "Shutting down in 5 seconds."
    elif "time" in command:
        return f"The current time is {get_time()}."
    elif "date" in command:
        return f"Today's date is {get_date()}."
    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        return search_wikipedia(query)
    elif "joke" in command:
        return tell_joke()
    else:
        return None

def assistant():
    """Main assistant loop"""
    print("Press 'q' to exit.")
    speak("Hello! How can I assist you today?", use_pyttsx3=True)
    
    while True:
        if keyboard.is_pressed("q"):
            print("Exiting...")
            speak("Goodbye! Have a great day!", use_pyttsx3=True)
            break

        user_input = listen()
        if not user_input:
            continue

        system_response = execute_command(user_input)
        if system_response:
            print(f"Assistant: {system_response}")
            speak(system_response, use_pyttsx3=True)
        else:
            response = gpt4_response(user_input)
            print(f"Assistant: {response}")
            speak(response, use_pyttsx3=True)

if __name__ == "__main__":
    assistant()
