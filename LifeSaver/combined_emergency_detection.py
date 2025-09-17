import random
import time
import speech_recognition as sr


# Function to simulate panic signals
def simulate_panic_signals():
    heart_rate = random.randint(60, 180)
    stress_level = random.uniform(0, 10)
    print(f"Heart rate: {heart_rate} bpm, Stress level: {stress_level:.2f}/10")

    heart_rate_threshold = 120
    stress_level_threshold = 7.0

    if heart_rate > heart_rate_threshold or stress_level > stress_level_threshold:
        print("Panic signal detected! Triggering emergency response...")
        return True
    return False


# Function to detect emergency keywords
def detect_keywords():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for emergency keywords (say 'help' or 'police')...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            speech_text = recognizer.recognize_google(audio).lower()
            print(f"You said: {speech_text}")

            if "help" in speech_text or "police" in speech_text:
                print("Emergency keyword detected!")
                return True
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Error in requesting speech recognition results.")
    return False


# Main function to check both panic signals and keywords
def check_emergencies():
    for i in range(5):
        print(f"\nReading {i + 1}:")

        # Check panic signals
        if simulate_panic_signals():
            print("Emergency response triggered due to panic signals!")
            return True

        # Check voice recognition for keywords
        if detect_keywords():
            print("Emergency response triggered due to detected keywords!")
            return True

        time.sleep(2)  # Pause between readings

    return False


# Run the emergency detection process
if check_emergencies():
    print("Emergency response initiated.")
else:
    print("No emergency detected.")
