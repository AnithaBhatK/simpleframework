from selenium_wrapper import SeleniumWrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class HomePage(SeleniumWrapper):
    _lnk_register = ("xpath", "//a[text()='Register']")
    _lnk_login  = ("xpath", "//a[text()='Log in']")
    _lnk_logout = ("xpath", "//a[text()='Log out']")

    def click_register(self):
        self.click_element(self._lnk_register)
    
    def click_login(self):
        self.click_element(self._lnk_login)
    
    def click_logout(self):
        self.click_element(self._lnk_logout)
    
    def is_user_logged_in(self, email):
        for _ in range(10):
            try:
                print(f'Trying to find element with link text {email}')
                return self.driver.find_element("xpath", f"//a[text()='{email}']").is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False
    
    def is_login_error_displayed(self, message):
        _xpath = f"//span[text()='{message}']"
        try:
            self.driver.find_element("xpath", _xpath)
            print(f'Error Message: {message} was displyed')
        except NoSuchElementException:
            return False
        else:
            return True