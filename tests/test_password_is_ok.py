from password_checker.password_check import Passwordcheck
password = "Freeze10%"
pass_checker = Passwordcheck(password)

def test_password_is_ok():
   assert pass_checker.lowercase() == True
def test_uppercase():
    assert pass_checker.uppercase() == True
def test_num_digits():
    assert pass_checker.num_digits() == True
def test_special_letter():
    assert pass_checker.special_letter() == True 