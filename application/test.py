import re

def validate_username(username):
    # Define the regex pattern for username validation
    pattern = r'^[a-zA-Z0-9_-]{3,16}$'
    
    # Check if the username matches the pattern
    if re.match(pattern, username):
        return True
    else:
        return False

username = input("Insert your name:")

validate_username()


