'''pracuje razem z plikiem conftest.'''

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("initialize_driver")
class Test_Druk():
    def test_lambdatest_simple_form_demo(self):
        # driver= webdriver.Chrome()
        # driver.maximize_window()
        self.driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
        message = 'Pytest is a test Framework'
        self.driver.find_element(By.ID, "user-message").send_keys(message)

        self.driver.find_element(By.ID,"showInput").click()
        message_text = self.driver.find_element(By.ID, "message").text
        assert message_text == message, f"message text nie zgadza sie z wpisanym tekstem"

        time.sleep(5)