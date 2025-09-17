import smtplib
import requests
import socket
from geopy.geocoders import Nominatim
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import time


# Function to get current location
def get_location():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(local_ip)
        return f"{location.latitude}, {location.longitude}" if location else "Location not found"
    except Exception as e:
        print(f"Error getting location: {e}")
        return "Location not found"


# Function to send emergency email using SendGrid
def send_email(subject, body, to_email):
    sendgrid_api_key = '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'  # Replace with your SendGrid API Key
    message = Mail(
        from_email='sunilbofl@gmail.com',  # Replace with your verified sender email
        to_emails=to_email,
        subject=subject,
        html_content=body
    )

    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(f"Email sent to {to_email}. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Main function to simulate emergency trigger
def main():
    print("Emergency initiated!")
    current_location = get_location()
    subject = "Emergency Alert!"
    body = f"<strong>Emergency Situation!</strong><br>Your location is: {current_location}"

    emergency_contacts = ["sunil199827@gmail.com", "sunilbofl@gmail.com"]  # Add your emergency contacts here
    for contact in emergency_contacts:
        send_email(subject, body, contact)

    print("Emergency emails sent.")


# Simulate triggering the emergency response
if __name__ == "__main__":
    main()
