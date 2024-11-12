import sqlite3

def login(username, password):
    # Connect to the database
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    
    try:
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"
        cursor.execute(query)
        
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

username = 'tester'
password = '123456'
login(username, password)
