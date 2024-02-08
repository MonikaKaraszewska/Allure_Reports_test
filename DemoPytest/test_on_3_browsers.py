'''pracuje razem z plikiem conftest.'''
import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("initialize_driver")
class BaseClass:
    driver = None

class Test_Drivers(BaseClass):
    def test_multiple_browser(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground/")
        header = self.driver.find_element(By.XPATH, "//div[@class = 'text-center pt-50']//h1").text
        print("Header: ", header)
        assert header == "Selenium Playground"
        time.sleep(20)
