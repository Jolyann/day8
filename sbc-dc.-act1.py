# Dictionary to store user data
users = {}

def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please choose another one.")
        return
    
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Login failed. Please check your username and password.")

def change_password():
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found.")
        return
    
    current_password = input("Enter your current password: ")
    if users[username] != current_password:
        print("Current password is incorrect.")
        return
    
    new_password = input("Enter your new password: ")
    users[username] = new_password
    print("Password changed successfully!")

# Main loop to interact with the user
while True:
    print("\na. Register\nb. Login\nc. Change Password\nd. Exit")
    choice = input("Enter your choice (a/b/c/d): ")

    if choice == 'a':
        register()
    elif choice == 'b':
        login()
    elif choice == 'c':
        change_password()
    elif choice == 'd':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a, b, c, or d.")
