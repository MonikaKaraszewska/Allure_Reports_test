import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_lambdatest_ecommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://ecommerce-playground.lambdatest.io/")
    search_word = 'iPhone'
    driver.find_element(By.XPATH, "//input[@placeholder='Search For Products']")\
        .send_keys(search_word)
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    # search_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Search - ')]").text
    # assert search_text == f'Search - {search_word}'

    search_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Search')]").text
    assert search_word in search_text, 'Search text is not correct'
    time.sleep(20)

    print(search_text)
