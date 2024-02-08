import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

pytestmark = [pytest.mark.regression,pytest.mark.sanity]

# pytestmark = pytest.mark.regression
@pytest.mark.integration

@pytest.mark.smoke
def test_lambda_ajax_form():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")
    driver.find_element(By.ID, "title").send_keys("Pytest Tutorial")

    driver.find_element(By.ID, "description").send_keys("Lambda Test Selenium Playground")

    driver.find_element(By.ID, "btn-submit").click()
    request = driver.find_element(By.ID, "submit-control").text
    assert request.__contains__("Processing")

def test_e2e():
    print("End to End Test")

@pytest.mark.smoke
def test_login():
    print("log in to Application")

@pytest.mark.kot
def test_logout():
    print("log OUT")