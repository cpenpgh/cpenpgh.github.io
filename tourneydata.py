'''
import requests

# Set the API URL
url = "https://next.matchplay.events/api/tournaments?series=API_KEY"
key = "/private/key"


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
'''
import requests
import json

#Which Tournaments are we looking for
t_id = "2704"

# Read the API key from a local file
with open("api_key.txt", "r") as f:
    api_key = f.readline().strip()

# Create a requests.Session object
session = requests.Session()

# Set the API key as a header
session.headers["Authorization"] = "Bearer " + api_key

# Make a request to the API
response = session.get("https://next.matchplay.events/api/tournaments?series=" + t_id)

# Check the response status code
if response.status_code == 200:
    # The request was successful, so parse the response body
    response_body = json.loads(response.content)

    # Do something with the response body
    print(response_body)
else:
    # The request failed, so print the error message
    print(response.content)