import random
import time


# Function to simulate panic signals (e.g., elevated heart rate or stress level)
def simulate_panic_signals():
    # Simulating heart rate data
    heart_rate = random.randint(60, 180)  # Random heart rate between 60 and 180 beats per minute
    stress_level = random.uniform(0, 10)  # Random stress level between 0 and 10 (simulated scale)

    print(f"Heart rate: {heart_rate} bpm, Stress level: {stress_level:.2f}/10")

    # Define thresholds for panic signals
    heart_rate_threshold = 120  # If heart rate > 120 bpm, it indicates panic
    stress_level_threshold = 7.0  # If stress level > 7.0, it indicates panic

    # Trigger an emergency if the heart rate or stress level crosses the threshold
    if heart_rate > heart_rate_threshold or stress_level > stress_level_threshold:
        print("Panic signal detected! Triggering emergency response...")
        return True
    else:
        print("No panic detected.")
        return False


# Simulate panic signals in a loop
for i in range(5):  # Simulate 5 readings over time
    print(f"\nReading {i + 1}:")
    if simulate_panic_signals():
        print("Emergency response triggered due to panic signals!")
    else:
        print("No emergency response needed.")

    time.sleep(2)  # Pause for 2 seconds between readings
