import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
class AssertionTest():
    pass

def test_Lambdatest_radio_button_demo_value():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    driver.find_element(By.XPATH, "//h4[contains(text(), 'Gender')]"
                                  "//following::input[@value='Female']").click()

    driver.find_element(By.XPATH, "//h4[contains(text(), 'Age')]"
                                  "//following::input[@value='5 - 15']").click()

    driver.find_element(By.XPATH, "//h4[contains(text(), 'Gender')]//following::input[@value='Female']"
                                  "//following::button").click()

    gender = driver.find_element(By.CSS_SELECTOR, ".genderbutton").text
    age = driver.find_element(By.CSS_SELECTOR, ".groupradiobutton").text
    zakres = re.findall(r'\d+',age)
    result_tuple = tuple(map(int, zakres))

    assert gender == 'Female', f'Gender is not correct'

    assert age == '5 - 15', f'Wybralismy "5 - 15", a jest {age}'

    assert 14 in range(*result_tuple), "age group  not correct"

    assert driver.title.__contains__("Selenium Grid Online")


