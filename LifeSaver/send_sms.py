from twilio.rest import Client

# Function to send an SMS
def send_sms(body, to_phone):
    account_sid = "your_account_sid"  # Replace with your Twilio Account SID
    auth_token = "your_auth_token"    # Replace with your Twilio Auth Token
    from_phone = "+447448726351"  # Replace with your Twilio phone number

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=body,
            from_=from_phone,
            to=to_phone
        )
        print(f"SMS sent to {to_phone}. Message SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

# Example usage of send_sms function
body = "Emergency! The current location is: Latitude 37.7749, Longitude -122.4194"
to_phone = "+(919542003874"  # Replace with the actual contact phone number
send_sms(body, to_phone)
