import speech_recognition as sr

# Function to detect emergency keywords like 'help' or 'police'
def detect_keywords():
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening for emergency keywords (say 'help' or 'police')...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Capture audio input

        try:
            # Convert speech to text using Google Web Speech API
            speech_text = recognizer.recognize_google(audio).lower()
            print(f"You said: {speech_text}")

            # Check if the speech contains emergency keywords
            if "help" in speech_text or "police" in speech_text:
                print("Emergency keyword detected!")
                return True
            else:
                print("No emergency detected.")
                return False

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            print("Error: Could not request results from the Speech Recognition service.")

# Call the function to listen for emergency keywords
if detect_keywords():
    print("Emergency response triggered! Sending alert...")
else:
    print("No emergency detected.")
