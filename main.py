import json

# Save the user data to the file
def save_users():
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)  # Write the data in a readable format

# Load users from the JSON file
def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Check if the username and password match
def login(username, password):
    if username in users and users[username]["password"] == password:
        return True
    return False

# Create a new user and save it to the file
def create_user(username, password):
    if username in users:
        print("Username already exists!")  # If the username already exists, show an error
        return False
    users[username] = {"password": password}  # Add the new user to the dictionary
    save_users()  # Save the updated data to the file
    print(f"User {username} created successfully!")
    return True

def main():
    # Load existing users
    global users
    users = load_users()

    while True:
        print("\n-- Welcome to the Login System --")
        action = input("Do you want to login (L), create a user (C), or quit (Q)? ").strip().lower()

        if action == "l":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if login(username, password):
                print("Login successful! ")
            else:
                print("Invalid username or password.")
        
        elif action == "c":
            username = input("Choose a username: ").strip()
            password = input("Choose a password: ").strip()
            create_user(username, password)
        
        elif action == "q":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try L, C, or Q.")

if __name__ == "__main__":
    main()
