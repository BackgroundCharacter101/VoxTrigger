import speech_recognition as sr
import webbrowser  # To open the default browser
import pyttsx3  # Text-to-speech

# Text-to-Speech setup
engine = pyttsx3.init()

# Function for speech feedback


def speak(message):
    print(f"Bot: {message}")
    engine.say(message)
    engine.runAndWait()

# Function to open default browser with a specific URL (Rick Roll)


def open_rick_roll():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll URL
    try:
        print(f"Opening browser with Rick Roll: {url}")
        webbrowser.open(url)  # Opens the Rick Roll video in default browser
        speak("Opening the video now.")
    except Exception as e:
        print(f"Error: {e}")
        speak("Failed to open the video.")

# Listen for command


def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                # Listening for speech command
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(
                    audio).lower()  # Convert speech to text
                print(f"Command detected: {command}")

                # If 'hello' is detected, open the Rick Roll video
                if "open rick and roll" in command:
                    print("Command 'hello' detected!")
                    speak("Opening the video now.")
                    open_rick_roll()  # Open the Rick Roll video when "hello" is detected
            except sr.WaitTimeoutError:
                pass  # Ignore timeout errors
            except sr.UnknownValueError:
                pass  # Ignore if speech was unclear
            except sr.RequestError:
                print("Error with speech recognition service.")


# Run the command listener
if __name__ == "__main__":
    listen_for_command()
