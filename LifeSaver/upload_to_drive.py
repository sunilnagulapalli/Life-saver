from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_to_drive(filename):
    # Google authentication
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Create local webserver and auto handles authentication

    drive = GoogleDrive(gauth)

    # Upload file to Google Drive
    file = drive.CreateFile({'title': filename})
    file.SetContentFile(filename)
    file.Upload()

    print(f"File '{filename}' uploaded to Google Drive.")

# Example usage
upload_to_drive("emergency_video.avi")
upload_to_drive("emergency_audio.wav")
