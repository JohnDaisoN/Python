import re


class InvalidPhoneNumber(Exception):
    """Exception raised for invalid phone number format."""

def validate(phone_number):
    
    if len(str(phone_number) )!= 10:
        raise InvalidPhoneNumber(phone_number)

def main():
    phone_numbers = [100000, 123, 9946404666]

    for phone_number in phone_numbers:
        try:
            validate(phone_number)
            print('Phone number is valid -  Indian format:', phone_number)
        except InvalidPhoneNumber as ph:
            print(f"International code detected - invalid number: {ph}")

if __name__ == "__main__":
    main()
