def login(username, password):
    # Fake user store
    users = {"alice": "password123", "bob": "secret"}

    if username not in users:
        return "Invalid credentials"

    if users[username] != password:
        return "Invalid credentials"

    return "Login successful"
