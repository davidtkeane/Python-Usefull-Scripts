import subprocess
import requests
import whois

# Use 'curl' to fetch your public IP address
try:
    ip_address = subprocess.check_output(['curl', '--insecure', 'https://ipinfo.io/ip'], text=True).strip()
except subprocess.CalledProcessError as e:
    print("Error fetching IP address using 'curl':", e)
    exit(1)

# API endpoint to fetch location information
api_url = f"https://ipinfo.io/{ip_address}/"

try:
    # Send an HTTP GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the desired information
        print("My IP Address")
        print("IP address:", data.get('ip'))
        print("Hostname:", data.get('hostname'))
        print("IP Address Location")
        print("Country:", data.get('country'))
        print("State/Region:", data.get('region'))
        print("City:", data.get('city'))
        print("ISP:", data.get('org'))
        print("Network:", data.get('asn'))
        print("Usage Type:", data.get('usage'))
        print("Timezone:", data.get('timezone', 'N/A'))  # Added "timezone" with a default value
        print("Local Time:", data.get('datetime'))
        print("Coordinates:", data.get('loc'))
        print("Postal:", data.get('postal', 'N/A'))  # Added "postal" with a default value

        # Perform a WHOIS lookup using the 'whois' command
        print("\nIP Address Whois")
        whois_output = subprocess.check_output(['whois', ip_address], text=True)
        print(whois_output)

    else:
        print("Failed to fetch data from the API. Status code:", response.status_code)

except Exception as e:
    print("An error occurred:", str(e))
