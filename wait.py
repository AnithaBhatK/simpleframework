from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

def wait(func):
    def wrapper(*args, **kwargs):
        instance, locator = args # args = (self, locator)
        w = WebDriverWait(instance.driver, 10)
        w.until(visibility_of_element_located(locator))
        return func(*args, **kwargs)
    return wrapper