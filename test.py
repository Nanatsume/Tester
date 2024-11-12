from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    # Check if the user has a session cookie
    session_cookie = request.cookies.get('session_id')
    if session_cookie:
        return f"Welcome back! Your session ID is {session_cookie}"
    else:
        return "Hello, please log in."

@app.route('/login', methods=['POST'])
def login():
    # Simulate a simple login where we set a session cookie
    username = request.form['username']
    password = request.form['password']
    
    # Here we are "mocking" a login process. In a real app, you'd authenticate users here.
    if username == "admin" and password == "password123":
        # Insecure: setting cookie without the Secure or HttpOnly flags
        resp = make_response(f"Logged in as {username}")
        resp.set_cookie('session_id', 'mock_session_id_value')
        return resp
    else:
        return "Invalid credentials", 401

@app.route('/logout')
def logout():
    # Insecure: logging out by clearing the session cookie
    resp = make_response("You have been logged out.")
    resp.delete_cookie('session_id')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
