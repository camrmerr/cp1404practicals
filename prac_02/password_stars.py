"""
CP1404 Password Stars
Program to check a password against minimum length
and then print stars equal to the password length
"""


def main():
    """Password Stars Program"""
    minimum_password_length = 8
    password = valid_password(minimum_password_length)
    print_password_stars(password)


def valid_password(minimum_password_length):
    """Get a valid password with a minimum required length"""
    password = input("Password: ")
    while len(password) < minimum_password_length:
        print("Password too short")
        password = input("Password:")
    return password


def print_password_stars(password):
    """Print the password length as asterisks"""
    print("*" * len(password))


main()