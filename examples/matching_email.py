import re

# text = "Please contact me at +91-(123)-456-7890 or via email ay john@example.com"
# john@example.com

pattern = r"\b[A-Za-z0-9._%+-]+@+[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

email = input("Enter email address: ")

if re.match(pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")
