from selenium import webdriver
from pytest import fixture

@fixture
def _driver():
    driver = webdriver.Chrome("./chromedriver")
    driver.get("http://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    driver.close()
