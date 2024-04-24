import re


class InvalidPhoneNumber(Exception):
    """Exception raised for invalid phone number format."""

def validate(phone_number):
    pattern = r'^(\+\d{1,3}\s?)?(\d{10})$'

    if not re.match(pattern, str(phone_number)):
        raise InvalidPhoneNumber(phone_number)

def main():
    try:
        validate(100000)  # This will raise an exception
        print('phone number is valid')
              # This will raise an exception
    except InvalidPhoneNumber as ph:
        print(f"Invalid phone number: {ph}")

    try:
        validate(123)  # This will raise an exception
        print('phone number is valid')
              # This will raise an exception
    except InvalidPhoneNumber as ph:
        print(f"Invalid phone number: {ph}")

    try:
        validate(9946404666)  # This will raise an exception
        print('phone number is valid')
              # This will raise an exception
    except InvalidPhoneNumber as ph:
        print(f"Invalid phone number: {ph}")

if __name__ == "__main__":
    main()
