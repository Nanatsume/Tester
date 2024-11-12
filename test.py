import sqlite3

def insecure_login(username, password):
    """
    Demonstrates an insecure login function vulnerable to SQL injection.

    Args:
        username (str): The username to log in.
        password (str): The password to log in.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    # Connect to the database
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    
    try:
        # Insecure SQL query vulnerable to SQL injection
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"
        cursor.execute(query)
        
        # If a record is found, login is successful
        user = cursor.fetchone()
        if user:
            print("Login successful!")
            return True
        else:
            print("Login failed.")
            return False

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        connection.close()

# Example usage (replace with actual test values)
username = "admin' --"
password = "anything"  # This will bypass the password check with SQL injection
insecure_login(username, password)
