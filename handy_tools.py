def value_checker(value):
    if value.isnumeric():
        return True, value
    else:
        return False, value


def api_authentication():
    print("-AUTHORIZATION IS REQUIRED ENTER YOUR CREDENTIALS-")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

