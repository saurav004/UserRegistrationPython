import re


class Validator:

    FIRST_AND_LAST_NAME_PATTERN = "^[A-Z]{1}[a-zA-Z]{2,30}$"

    @classmethod
    def collect_and_validate_first_name(cls):
        first_name = input("Enter first Name : ")
        if re.fullmatch(Validator.FIRST_AND_LAST_NAME_PATTERN, first_name):
            print(f"First Name validated, HI {first_name}")
        else:
            print("Invalid First Name !!!")
            Validator.collect_and_validate_first_name()


if __name__ == "__main__":
    print("Welcome to User Registration Program")
    Validator.collect_and_validate_first_name()
