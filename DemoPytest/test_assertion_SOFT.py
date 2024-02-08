import time
import re

import pytest
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AssertionTest(softest.TestCase):
    pass

    def test_radio_button_demo_value_SOFT(self):
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
        zakres = re.findall(r'\d+', age)
        result_tuple = tuple(map(int, zakres))
        # tuple_2 = (0, 1)
        # correct_tuple = tuple(sum(pair) for pair in zip(result_tuple, tuple_2))
        idx_results_tuple = (result_tuple[0] , result_tuple[1] +1)

        arg = 15
        self.soft_assert(self.assertTrue, arg in range(*idx_results_tuple), f" {arg} not in range {result_tuple}")

        # self.soft_assert(self.assertIs,
        #     "Male",gender, f'Gender is not correct')

        self.soft_assert(self.assertTrue,
                         gender.__contains__("Female"), f'Gender is not correct')

        self.soft_assert(self.assertTrue, driver.title.__contains__("Selenium Grid Online"))

        # self.soft_assert(self.assertIn, "10", age, "age group  not correct")

        self.assert_all()


