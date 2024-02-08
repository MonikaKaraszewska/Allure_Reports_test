import math

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")

@pytest.mark.parametrize("num1,num2, expected_total", [
        (25, 25, 50),
        (10, 10, 30),
        (30, 40, 70)
])

def test_lambdatest_two_input_fields(num1, num2, expected_total):
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    driver.find_element(By.ID, "sum1").send_keys(num1)
    driver.find_element(By.ID, "sum2").send_keys(num2)
    driver.find_element(By.XPATH, "//button[text()='Get Sum']").click()
    suma = driver.find_element(By.ID, "addmessage").text
    suma = int(suma)
    assert suma == expected_total, "Actual and Expected do not match"


@pytest.mark.parametrize("base", [1,2,3])
@pytest.mark.parametrize("exponent", [4,5,6])
def test_raising_base_to_power(base,exponent):
    result = base ** exponent
    assert result == math.pow(base, exponent)