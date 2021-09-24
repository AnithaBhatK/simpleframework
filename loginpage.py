from selenium_wrapper import SeleniumWrapper

class LoginPage(SeleniumWrapper):
    # Class Vairables
    _txt_email = ("id", "Email")
    _txt_password = ("id", "Password")
    _btn_login = ("xpath", "//input[@value='Log in']")
    _lbl_invalid_credentails = ("xpath", "//span[text()='Login was unsuccessful. Please correct the errors and try again.']")

    def enter_email(self, email):
        self.enter_text(self._txt_email, value=email)
    
    def enter_password(self, password):
        self.enter_text(self._txt_password, value=password)
    
    def click_login(self):
        self.click_element(self._btn_login)

        