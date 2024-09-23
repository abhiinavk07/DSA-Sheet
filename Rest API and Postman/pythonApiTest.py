# This script is a simple example to test a REST API using Python.
# This script we can either get from postman code section or use coPilot


# Step 1: Install the requests library using pip
# Command: pip install requests

# Step 2: Import the requests library
import requests

# Step 3: Define the URL of the API
api_url = 'https://simple-books-api.glitch.me/books'

# Step 4: Create a function to make a GET request
def check_status_code():
    try:
        # Step 5: Make the GET request
        response = requests.get(api_url)

        # Step 6: Check if the response status is 200
        if response.status_code == 200:
            # Step 7: Log success message
            print('Success: Status code is 200')
            print('Response:', response.json())
        else:
            # Log failure message
            print(f'Failure: Status code is {response.status_code}')
            print('Response:', response.json())
    except requests.RequestException as e:
        # Handle errors
        print('Error making the request:', e)

# Call the function
check_status_code()