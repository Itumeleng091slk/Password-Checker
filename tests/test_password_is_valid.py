# import pytest
from password_checker.password_check import Passwordcheck
password = "Freez1$l"
pass_checker = Passwordcheck(password)

def test_password_is_valid():
    assert pass_checker.lowercase() == True
def test_uppercase():
    assert pass_checker.uppercase() == True
def test_num_digits():
    assert pass_checker.num_digits() == True
def test_special_letter():
    assert pass_checker.special_letter() == True
def test_length_of_password():
    assert pass_checker.length_of_password() == True

# def test_length():
#     assert pass_checker.length() >= 8
   

   

