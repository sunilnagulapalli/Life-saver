import socket
from geopy.geocoders import Nominatim
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import smtplib
from email.mime.text import MIMEText

# Function to send an email
def send_email(subject, body, to_email):
    sendgrid_api_key = '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'  # Replace with your SendGrid API Key
    message = Mail(
        from_email='sunilbofl@gmail.com',  # Replace with your verified sender email
        to_emails=to_email,
        subject=subject,
        html_content=body
    )

    # Connect to Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage of send_email function
subject = "Emergency Alert"
body = "This is a test of the emergency alert system. The current location is: Latitude 37.7749, Longitude -122.4194"
to_email = "sunil199827@gmail.com"  # Replace with the actual contact email
send_email(subject, body, to_email)
