import os

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.filepath = os.path.join(os.path.dirname(__file__), "users.txt")  # Full path to users.txt

    @staticmethod
    def sign_up(username, password):
        if not username or not password:
            return "Please enter both username and password."

        filepath = os.path.join(os.path.dirname(__file__), "users.txt")  # Full path to users.txt
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                existing_users = file.readlines()
                existing_users = [user.strip().split(":")[0] for user in existing_users]
                if username in existing_users:
                    return "Username already exists. Please choose another one."

        with open(filepath, "a") as file:
            file.write(f"{username}:{password}\n")

        return "User signed up successfully!"

    @staticmethod
    def login(username, password):
        if not username or not password:
            return "Please enter both username and password."

        filepath = os.path.join(os.path.dirname(__file__), "users.txt")  # Full path to users.txt
        if not os.path.exists(filepath):
            return "No users found. Please sign up first."

        with open(filepath, "r") as file:
            users = file.readlines()

        for user in users:
            stored_username, stored_password = user.strip().split(":")
            if username == stored_username and password == stored_password:
                return "Login successful!"

        return "Invalid username or password."
    
