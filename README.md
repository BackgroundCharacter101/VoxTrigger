# VoxTrigger
VoxTrigger - Voice Activated Browser Launcher

VoxTrigger is a simple Python-based voice command tool that listens for a specific keyword ("hello" by default)
and immediately opens a web browser to a predefined URL. It's designed to be lightweight, responsive, and easily
modifiable by beginners or tinkerers who want to explore voice automation with Python.

How It Works:
-------------
1. The script uses the `speech_recognition` library to capture voice input through your microphone.
2. When you say the keyword (default is "hello"), it recognizes the word using Google's speech-to-text API.
3. Once the keyword is detected, it uses the `subprocess` module to launch your default web browser or a specified one.
4. At the same time, it gives audio feedback using `pyttsx3`, a text-to-speech engine.

Customization Options:
----------------------
- Change the Trigger Word:
  Modify the line: `if "hello" in command:`
  Example: To trigger on the word "start", change it to: `if "start" in command:`

- Change the URL:
  Modify the variable: `url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"`
  You can insert any URL, including your own local apps or dashboards.

- Change the Voice Feedback:
  Modify the `speak()` function call, e.g., `speak("Opening the video now")`
  Replace the message with your own response.

Dependencies:
-------------
- Python 3.10+
- speech_recognition
- pyttsx3
- pyaudio (must be installed separately due to portaudio dependency)

Use Case Ideas:
---------------
- Panic Button that opens distraction videos or fun content
- Custom voice launcher for web apps or links
- Expandable into a full voice-assistant

This project is built for educational purposes and to help you explore speech automation in a fun and direct way.
Project Credits:  
- Created by BackgroundCharacter101
