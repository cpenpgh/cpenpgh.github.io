import requests

# Set the API URL
url = "https://next.matchplay.events=API_KEY"

# Make a GET request to the API
response = requests.get(url)

# Check the response status code
if response.status_code == 200:
    # The request was successful, so parse the JSON response
    data = response.json()

    # Do something with the information
    print("This is the", data["player"][0]["description"])
else:
    # The request failed, so print an error message
    print("Error connecting to the API:", response.status_code)