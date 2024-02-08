import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_lambdatest_simple_form_demo():
    driver= webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    message = 'Pytest is a test Framework'
    driver.find_element(By.ID, "user-message").send_keys(message)

    driver.find_element(By.ID,"showInput").click()
    message_text = driver.find_element(By.ID, "message").text
    assert message_text == message, f"message text nie zgadza sie z wpisanym tekstem"

    time.sleep(5)