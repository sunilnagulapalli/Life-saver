import cv2

# Function to record video for a specified duration
def record_video(filename="emergency_video.avi", record_seconds=5):
    # Initialize the video capture object
    cap = cv2.VideoCapture(0)  # '0' is the default camera

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    print("Recording video...")

    # Record video for the specified duration
    for _ in range(int(20 * record_seconds)):
        ret, frame = cap.read()  # Capture frame-by-frame
        if ret:
            out.write(frame)  # Write the frame to the file
            cv2.imshow('Recording...', frame)  # Display the recording window
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit with 'q' key
                break
        else:
            break

    # Release the camera and close the window
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Video recorded and saved as {filename}")

# Test the function
record_video()
