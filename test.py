import requests
from requests.exceptions import HTTPError, Timeout
import logging

logging.basicConfig(level=logging.INFO)

def login_to_website(url, username, password):
    """
    Logs into a website and returns the response object.

    Args:
        url (str): The login URL.
        username (str): The username for login.
        password (str): The password for login.

    Returns:
        response (requests.Response): The response object from the login attempt.
    """
    try:
        login_data = {
            'username': username,
            'password': password
        }

        # Sending a POST request to the login URL with the login data
        response = requests.post(url, data=login_data, timeout=10)
        
        # Raise an error for unsuccessful status codes
        response.raise_for_status()

        if "login successful" in response.text.lower():
            logging.info("Login successful!")
        else:
            logging.warning("Login failed. Check credentials or login URL.")
            
        return response

    except HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Timeout as timeout_err:
        logging.error(f"Request timed out: {timeout_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")
    return None


# Example usage (make sure to replace with real values)
url = "https://example.com/login"
username = "your_username"
password = "your_password"

login_response = login_to_website(url, username, password)

if login_response:
    logging.info("Process completed.")
else:
    logging.error("Login attempt failed or error occurred.")
