import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)

# pytestmark = pytest.mark.skip(reason="Tests in this module are skipped, Bo OUP zablokowało mnie .")  # tyczy sie całego modulu i nie wykonuje
    # wszystkich testów z tego pliku/modulu, ale nie dziw sie bo przegladarka i tak sie otworzy bo musi sprawdzic czy cos jest do zrobienia
# jakby była utworzona klasa to wystarczy nad klasa napisac @pytest.mark.skip(reason="This test is skipped, Bo tak.") i ominie cała klase
def start_automatic_fixtrure():
    print("start_automatic_fixtrure".upper())

def setup_teardown_method():
    driver.get("https://elt.oup.com/")
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

# @pytest.mark.skip(reason="This test is skipped, Bo tak.")  # skip nie wykonuje tylko tego testu przed ktorym jest

def test1_title_after_logIn():
    assert driver.title == 'Your Profile', f"The title of the page 'Your Profile' is NOT correct"

def test2_change_password_title():

    driver.find_element(By.ID, "changePasswordLink").click()
    assert driver.title == 'Change password', f"The title of the page 'Change password' is NOT correct"