from loginpage import LoginPage
from homepage import HomePage
from pytest import mark
from time import sleep

headers = "email,password"
data = [("bill.gates@company.com", "Password123"), ("steve.jobs@company.con", "Password123")]

@mark.parametrize(headers, data)
def test_login_positive(_driver, email, password):
    # Click on Login Link
    hp = HomePage(_driver)
    hp.click_login()
    # Login
    lp = LoginPage(_driver)
    lp.enter_email(email)
    lp.enter_password(password)
    lp.click_login()
    assert hp.is_user_logged_in(email) == True


headers = "email,password,expected_message"
data = [("bill.gates@company.com", "Password12", "Login was unsuccessful. Please correct the errors and try again."), 
("steve.jobs", "Password123", "Please enter a valid email address.")
]

@mark.parametrize(headers, data)
def test_login_negative(_driver, email, password, expected_message):
    # Click on Login Link
    hp = HomePage(_driver)
    hp.click_login()
    # Login
    lp = LoginPage(_driver)
    lp.enter_email(email)
    lp.enter_password(password)
    lp.click_login()
    sleep(5)
    assert hp.is_login_error_displayed(expected_message) == True