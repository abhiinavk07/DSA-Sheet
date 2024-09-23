// Step 1: Install Axios using npm
// Command: npm install axios

// Step 2: Import Axios
const axios = require('axios');

// Step 3: Define the URL of the API
const apiUrl = 'https://api.example.com/data';

// Step 4: Create a function to make a GET request
async function checkStatusCode() {
  try {
    // Step 5: Make the GET request
    const response = await axios.get(apiUrl);

    // Step 6: Check if the response status is 200
    if (response.status === 200) {
      // Step 7: Log success message
      console.log('Success: Status code is 200');
    } else {
      // Log failure message
      console.log(`Failure: Status code is ${response.status}`);
    }
  } catch (error) {
    // Handle errors
    console.error('Error making the request:', error);
  }
}

// Call the function
checkStatusCode();