from registrationpage import RegistrationPage
from homepage import HomePage
from pytest import mark

headers = "gender,firstname,lastname,email,password"
data = [("male", "steve", "jobs", "steve.jobs@company.com", "Password123"), 
        ("female", "bill", "gates", "bill.gates@company.con", "Password123")]

@mark.parametrize(headers, data)
def test_registration(_driver, gender, firstname, lastname, email, password):
    hp = HomePage(_driver)
    hp.click_register()

    rp = RegistrationPage(_driver)
    if gender == "male":
        rp.select_male()
    else:
        rp.select_female()
        
    rp.enter_fname(firstname)
    rp.enter_lname(lastname)
    rp.enter_email(email)
    rp.enter_password(password)
    rp.enter_confirm_password(password)
    rp.click_register()