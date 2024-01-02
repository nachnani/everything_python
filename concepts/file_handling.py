import json
import os


def save_user_data():
    user_list = []

    while True:
        # Accept user input for name, email, and contact
        name = input("Enter name (or 'quit' to exit): ")

        if name.lower() == "quit":
            break

        email = input("Enter email: ")
        contact = input("Enter contact: ")

        # Create a dictionary with the user data
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }

        user_list.append(user_data)

    if os.path.exists("user_data.json"):
        # Load existing user data from the file
        with open("user_data.json", "r") as file:
            existing_data = json.load(file)

        # Append the new user data to the existing data
        user_list.extend(existing_data)

    # Open the file in write mode and save the user data as JSON
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)

    print("User data saved successfully!")


def read_user_data():
    # Check if the file exists
    if not os.path.exists("user_data.json"):
        print("No user data found.")
        return

    # Open the file in read mode
    with open("user_data.json", "r") as file:
        # Load the JSON data
        user_list = json.load(file)

    # Print the user data
    print("User Data:")
    for user_data in user_list:
        print("Name:", user_data["name"])
        print("Email:", user_data["email"])
        print("Contact:", user_data["contact"])
        print()


def edit_user_data(name):
    # Check if the file exists
    if not os.path.exists("user_data.json"):
        print("No user data found.")
        return

    # Open the file in read mode
    with open("user_data.json", "r") as file:
        # Load the JSON data
        user_list = json.load(file)

    user_found = False

    # Search for the user based on the name
    for user_data in user_list:
        if user_data["name"].lower() == name.lower():
            # Prompt the user for updated email and contact
            email = input("Enter updated email: ")
            contact = input("Enter updated contact: ")

            # Update the user data
            user_data["email"] = email
            user_data["contact"] = contact

            user_found = True
            break

    if not user_found:
        print("User not found.")

    # Open the file in write mode and save the updated user data as JSON
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)

    print("User data updated successfully!")


def delete_user_data(name):
    # Check if the file exists
    if not os.path.exists("user_data.json"):
        print("No user data found.")
        return

    # Open the file in read mode
    with open("user_data.json", "r") as file:
        # Load the JSON data
        user_list = json.load(file)

    user_found = False

    # Search for the user based on the name
    for user_data in user_list:
        if user_data["name"].lower() == name.lower():
            # Remove the user data from the list
            user_list.remove(user_data)

            user_found = True
            break

    if not user_found:
        print("User not found.")

    # Open the file in write mode and save the updated user data as JSON
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)

    print("User data deleted successfully!")


# Save user data
save_user_data()

# Read user data from file
read_user_data()

# Edit user data
edit_name = input('Enter name which you want to edit')
edit_user_data(edit_name)  # Pass the name of the user you want to edit

# Read user data again to verify the changes
read_user_data()

# Delete user
delete_user = input('Enter the name of user you want to delete')
delete_user_data(delete_user)