import string
import random

def simple_pass(pass_len):
    """
    Creates a simple password.
    Parameter "pass_len" is the character length of the password to be created.
    """
    characters = string.ascii_letters + string.digits
    # Picks a random mandatory number.
    mandatory_number = str(random.randint(0, 9))
    # Picks a random mandatory lowercase.
    mandatory_lowercase = string.ascii_lowercase
    mandatory_lowercase = ''.join(random.choice(mandatory_lowercase) for i in range(1))
    # Picks a random mandatory uppercase.
    mandatory_uppercase = string.ascii_uppercase
    mandatory_uppercase = ''.join(random.choice(mandatory_uppercase) for i in range(1))
    # Randomly choices characters from the characters variable.
    password =  "".join(random.choice(characters) for x in range(pass_len - 3))
    # Concatenates the password variable with the three mandatory variables.
    password = password + mandatory_number + mandatory_lowercase + mandatory_uppercase
    return password

# Calls the simple_pass function. Modify the 8 if you want a different password length.
# for loop to create 99 passwords
for i in range(100):
    password = simple_pass(8)
    print(password)




