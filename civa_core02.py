# civa_core.py

import os
import threading
import traceback
import pyttsx3
import psutil
import subprocess
import webbrowser
import speech_recognition as sr
import google.generativeai as genai

# --- Configuration ---
GEMINI_API_KEY = "AIzaSyCLLIZGUr3ynZp1l4OJvvVoFVpCuS_7j_0"  # Replace with your Gemini 1.5 Flash API Key
MODEL_NAME = "gemini-1.5-flash-latest"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)
chat = model.start_chat(history=[])

# --- TTS Setup ---
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def speak(text):
    def _speak():
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"[TTS ERROR] {e}")
    threading.Thread(target=_speak).start()

# --- Listen (Voice Input) ---
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return recognizer.recognize_google(audio).lower()
        except:
            return ""

# --- Task Management ---
def execute_task(command: str) -> str:
    command = command.lower().strip()
    
    if "shutdown" in command:
        os.system("shutdown /s /t 30")
        return "Shutting down the system."

    elif "restart" in command:
        os.system("shutdown /r /t 30")
        return "Restarting the system."

    elif "open calculator" in command:
        subprocess.Popen("calc.exe")
        return "Calculator opened."

    elif "open notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Notepad opened."

    elif "browser" in command or "google" in command:
        webbrowser.open("https://www.google.com")
        return "Browser opened."

    elif "system status" in command:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        return f"System Status:\nCPU: {cpu}%\nMemory: {mem}%\nDisk: {disk}%"

    return None  # Not a system command

# --- Gemini Response ---
def get_response(user_input: str) -> str:
    task_result = execute_task(user_input)
    if task_result:
        return task_result
    try:
        response = chat.send_message(user_input)
        return response.text.strip()
    except Exception as e:
        return f"[ERROR] {traceback.format_exc()}"
