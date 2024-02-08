''' strona OUP zablokkwała mnie po tym jak kilkanascie razy puszczalam testy wutomatyczne.
    biblioteka requests pozwla na zamiane User-Agent w headers, i wyslac zadanie niby ze
    wysyłamy uzywajac przegladerki a nie requestes w pyton
    I tu własnie zaimplemnetowałam do testów, bo nie działały wczesniej'''


import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import requests


driver = webdriver.Chrome()
driver.implicitly_wait(10)

def start_automatic_fixture():
    print("start_automatic_fixtrure".upper())

@pytest.fixture(scope='module')
def setup_teardown_method():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get("https://elt.oup.com/", headers=headers)
    oupUrl = response.url

    driver.get(oupUrl)
    print("OUPRL :",oupUrl)
    print("Header: ", response.request.headers)
    driver.maximize_window()
    driver.find_element(By.XPATH, "//li[@class='horizontalNav_item hideSignedIn']//a[text() = 'Log in']").click()
    driver.find_element(By.ID,"username").send_keys("monikakaraszewska@gmail.com")
    driver.find_element(By.ID,"password").send_keys("Oxford58")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert driver.title == "Oxford Teachers' Club | Oxford University Press", f"The title after log in is not correct"
    time.sleep(5)
    driver.find_element(By.ID, "eacProfileLink").click()

    print("Log In")
    yield
    driver.find_element(By.XPATH, "//li[contains(text(),'Hello')]").click()
    try:
        driver.find_element(By.XPATH, "//a[text() = 'Log out']").click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//a[text() = 'Logout']").click()
    assert driver.title == "Log in"
    print("Log Out")

    time.sleep(10)

def test1_title_after_logIn(setup_teardown_method):
    assert driver.title == 'Your Profile', f"The title of the page 'Your Profile' is NOT correct"

def test2_change_password_title(setup_teardown_method):
    driver.find_element(By.ID, "changePasswordLink").click()
    assert driver.title == 'Change password', f"The title of the page 'Change password' is NOT correct"