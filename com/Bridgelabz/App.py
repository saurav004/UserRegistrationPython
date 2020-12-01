import re


class Validator:
    valid_emailIds = ["abc@yahoo.com", "abc-100@yahoo.com",
                      "abc.100@yahoo.com", "abc111@abc.com", "abc-100@abc.net", "abc.100@abc.com.au", "abc@1.com",
                      "abc@gmail.com.com", "abc+100@gmail.com"]

    invalid_emailIds = ["abc@.com.my", "abc123@gmail.a", "abc123@.com",
                        "abc123@.com.com", ".abc@abc.com", "abc()*@gmail.com", "abc..2002@gmail.com", "abc.@gmail.com",
                        "abc@abc@gmail.com", "abc@gmail.com.1a", "abc@gmail.com.aa.au"]

    FIRST_AND_LAST_NAME_PATTERN = "^[A-Z]{1}[a-zA-Z]{2,30}$"
    EMAIL_PATTERN = "^[a-zA-Z][a-zA-Z0-9_\\-+]*[.]{0,1}[a-zA-Z0-9_\\-+]{1,}[@][a-zA-Z0-9]{1,}[.][a-zA-Z]{2,}[.]{0,}[a-zA-Z]*$"
    MOBILE_NUMBER_PATTERN = "^[+]{1}[0-9]{2}[ ][6-9]{1}[0-9]{9}"
    PASSWORD_PATTERN_RULE1 = "^[a-zA-Z0-9]{8,}$"
    PASSWORD_PATTERN_RULE2 = "^(?=.*[A-Z]).{8,}$"
    PASSWORD_PATTERN_RULE3 = "^(?=.*[A-Z])(?=.*?[0-9]).{8,}$"
    PASSWORD_PATTERN_RULE4 = "^(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

    @classmethod
    def collect_and_validate_first_name(cls):
        """
        Objective:taking first name and matching it with respective pattern
        :rtype: void
        """
        first_name = input("Enter first Name : ")
        if re.fullmatch(Validator.FIRST_AND_LAST_NAME_PATTERN, first_name):
            print(f"First Name validated, HI {first_name}")
        else:
            print("Invalid First Name !!!")
            Validator.collect_and_validate_first_name()

    @classmethod
    def collect_and_validate_last_name(cls):
        """
        Objective:taking last name and matching it with respective pattern
        :rtype: void
        """
        last_name = input("Enter last Name : ")
        if re.fullmatch(Validator.FIRST_AND_LAST_NAME_PATTERN, last_name):
            print(f"Last Name validated")
        else:
            print("Invalid Last Name !!!")
            Validator.collect_and_validate_last_name()

    @classmethod
    def collect_and_validate_email(cls):
        """
        Objective:taking email Id and matching it with respective pattern
        :rtype: void
        """
        email = input("Enter Email ID : ")
        if re.fullmatch(Validator.EMAIL_PATTERN, email):
            print(f"Email Validated")
        else:
            print("Invalid Email !!!")
            Validator.collect_and_validate_email()

    @classmethod
    def collect_and_validate_mobile_number(cls):
        """
        Objective:taking mobile Number and matching it with respective pattern
        :rtype: void
        """
        mobile_number = input("Enter Mobile Number : ")
        if re.fullmatch(Validator.MOBILE_NUMBER_PATTERN, mobile_number):
            print(f"Mobile Number Validated")
        else:
            print("Invalid Mobile Number !!!")
            Validator.collect_and_validate_mobile_number()

    @classmethod
    def collect_and_validate_password(cls):
        """
        Objective:taking password and matching it with respective pattern
        :rtype: void
        """
        password = input("Enter Password : ")
        if re.fullmatch(Validator.PASSWORD_PATTERN_RULE4, password):
            print(f"Password Validated")
        else:
            print("Invalid Password !!!")
            Validator.collect_and_validate_password()

    @classmethod
    def validate_multiple_email(cls, email_id_array):
        """
        Objective:taking multiple email Id and matching it with respective pattern
        :rtype: void
        """
        for email in email_id_array:
            if re.fullmatch(Validator.EMAIL_PATTERN, email):
                print(f"{email}\t\t:Valid")
            else:
                print(f"{email}\t\t:Invalid")


if __name__ == "__main__":
    print("Welcome to User Registration Program")
    Validator.collect_and_validate_first_name()
    Validator.collect_and_validate_last_name()
    Validator.collect_and_validate_email()
    Validator.collect_and_validate_mobile_number()
    Validator.collect_and_validate_password()
    Validator.validate_multiple_email(Validator.valid_emailIds)
    Validator.validate_multiple_email(Validator.invalid_emailIds)
