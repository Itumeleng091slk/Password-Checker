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
            print("Passwords meets all required") 

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

    def password_is_ok(self, password):
        condition_pass = 0
        if len(password)==0:
            return False
        condition_pass +=1

        if len(password) <= 8:
            return False
        condition_pass += 1

        if self.num_digits() == True:
            condition_pass +=1

        if self.lowercase() == True:
            condition_pass +=1

        if self.special_letter() == True:
            condition_pass +=1

        if condition_pass >= 3:
            return True
        else:
            return False



if __name__== '__main__':

    password = "Geeks$1102"
    check_password = Passwordcheck(password)
    
    if(check_password.password_is_ok(password)== True):
        print("password is ok!")
    else:
        print("password is wrong")

    if(check_password.password_validate()== True):
        print("password is valid")
    else:
        print("password is invalid")

