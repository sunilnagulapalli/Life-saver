import random
import time
import geocoder
import speech_recognition as sr
import cv2
import pyaudio
import wave


# Function to get current location using IP
def get_location_by_ip():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng
    else:
        return None


def send_location(latitude, longitude):
    print(f"Sending location: Latitude: {latitude}, Longitude: {longitude}")
    print("Location sent to local authorities and emergency contact.")


# Function to record audio
def record_audio(filename="emergency_audio.wav", record_seconds=5):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    rate = 44100
    p = pyaudio.PyAudio()

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []

    for _ in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"Audio recorded and saved as {filename}")


# Function to record video
def record_video(filename="emergency_video.avi", record_seconds=5):
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    for _ in range(int(20 * record_seconds)):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('Recording...', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Video recorded and saved as {filename}")


# Simulate panic signals
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


# Main function to check for emergencies, record audio and video, and send location
def check_emergencies():
    for i in range(3):
        print(f"\nReading {i + 1}:")

        if simulate_panic_signals() or detect_keywords():
            print("Emergency response triggered!")
            location = get_location_by_ip()
            if location:
                latitude, longitude = location
                send_location(latitude, longitude)
            else:
                print("Could not retrieve location.")

            # Start recording audio and video
            record_audio()
            record_video()

            return True

        time.sleep(2)  # Pause between readings

    return False


# Run the emergency detection process
if check_emergencies():
    print("Emergency response initiated with location, audio, and video recording.")
else:
    print("No emergency detected.")
