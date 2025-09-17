pip install SpeechRecognition
pip install pyaudio


import speech_recognition as sr

# Function to detect emergency keywords
def detect_keywords():
    recognizer = sr.Recognizer()

    # Use the microphone as the source
    with sr.Microphone() as source:
        print("Listening for emergency keywords (say 'help' or 'police')...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for audio input

        try:
            # Convert speech to text
            speech_text = recognizer.recognize_google(audio).lower()
            print(f"You said: {speech_text}")

            # Check if any emergency keywords are present
            if "help" in speech_text or "police" in speech_text:
                print("Emergency keyword detected!")
                return True
            else:
                print("No emergency detected.")
                return False

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")

# Call the function
if detect_keywords():
    print("Sending alert to authorities...")
