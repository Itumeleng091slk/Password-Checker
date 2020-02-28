import re

class Passwordcheck(object):
#     def __init__(self):
#         pass

    def __init__(self, password): 
        self.password = str(password)
        
    def lowercase(self):
        lowercase = any (c.islower() for c in self.password)
        return lowercase

    def uppercase(self):
        uppercase = any (c.isupper()for c in self.password)
        return uppercase
 
    def special_letter(self):
        special_sym = "$ @ # %"
        special_sym = any (c in special_sym for c in self.password)
        return special_sym

           
    def num_digits(self):
        num_digits = any (c.isdigit() for c in self.password)
        return num_digits

    def length_of_password(self):
        length_of_password = len(self.password)
        length_of_password  <=8
        return length_of_password <= 8


    def password_validate(self):
        lowercase = self.lowercase()
        uppercase = self.uppercase()
        num_digits = self.num_digits()
        special_letter = self.special_letter()
        length_of_password = self.length_of_password()

        result = lowercase and uppercase and special_letter and num_digits and length_of_password <= 8

        if result:
            print("Passwords meets all necessary requirements") 
            return True

        elif not length_of_password <= 8:
            raise Exception("Password should be atleast eight characters long")

        elif not self.password == 0:
            raise Exception("Password should exist")

        elif not lowercase:
            raise Exception(" Password must have atleast one lowercase")
            return False
        
        elif not uppercase:
            return Exception("Password must have atleast one uppercase")
            return False
        
        elif not num_digits:
            raise Exception("Password must have atleast one digit/character")
            return False
        
        elif not special_letter:
             raise Exception("Password must have atleast one special character")
        else:
            pass

    def password_is_ok(self):
        """
        8 characters length 
        1 digit or more
        1 special letter or more
        1 uppercase or more
        1 lowercase or more
        """
        # self.password = str(password)
        length_error = len(self.password) <= 8
        there_is_num_digit_error = re.search(r"[0-9]", self.password) is None
        there_is_an_uppercase_error = re.search(r"[A-Z]", self.password) is None
        there_is_a_lowercase_error = re.search(r"[a-z]",self.password) is None
        there_is_a_special_letter_error = re.search(r"\W", self.password) is None
        password_is_ok = not (length_error and there_is_num_digit_error and there_is_an_uppercase_error) or (there_is_a_special_letter_error and length_error and there_is_a_lowercase_error )
        return {
            'password_is_ok':password_is_ok,
            'length_error':length_error,
            'there_is_num_digit_error': there_is_num_digit_error,
            'there_is_a_lowercase_error':there_is_a_lowercase_error,
            'there_is_a_special_letter_error ':there_is_a_special_letter_error,
        }
        
C = Passwordcheck("Geeks$10")
print(C.password_validate())
print(C.password_is_ok())       