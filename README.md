# CIVA - Computer Integrated Virtual Assistant

## Overview
CIVA is a desktop virtual assistant with both GUI and voice interaction capabilities. It uses Google's Gemini 1.5 Flash AI model for generating responses and can perform various system tasks.

## Features
- Text and voice-based interaction
- Modern GUI interface built with Tkinter
- System commands (shutdown, restart, open applications)
- System status monitoring (CPU, memory, disk usage)
- Web browsing capabilities
- AI-powered conversations using Google's Gemini 1.5 Flash

## Requirements
- Python 3.x
- Required packages: pyttsx3, psutil, speech_recognition, google-generativeai, tkinter

## Installation
```bash
pip install pyttsx3 psutil SpeechRecognition google-generativeai
```

## Usage
Run the GUI application:
```bash
python civa_gui.py
```

## Project Structure
- `civa_core02.py`: Core functionality including AI integration, voice processing, and system commands
- `civa_gui.py`: Tkinter-based graphical user interface

## Note
This project requires a valid Google Gemini API key to function properly.
