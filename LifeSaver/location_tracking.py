import geocoder

# Function to get the current location using the computer's IP address
def get_location_by_ip():
    g = geocoder.ip('me')  # Get location based on your public IP address
    if g.ok:
        return g.latlng  # Return latitude and longitude
    else:
        return None

# Get and print the current location
location = get_location_by_ip()

if location:
    latitude, longitude = location
    print(f"Current location (from IP): Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Could not retrieve location.")
