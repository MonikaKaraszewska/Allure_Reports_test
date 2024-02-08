import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




url = "https://www.globalsqa.com/demo-site/"
driver = webdriver.Chrome()



def test_page_title():
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    expected_title = "Demo Testing Site - GlobalSQA"
    assert driver.title == expected_title, 'The title of the page is not correct'
    print(driver.title)

def test_first_step_elements():
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    first_step_elements = driver.find_elements(By.XPATH,"//li[text()='First Step']//following::li[position()<7]")
    text_elements = ['Tabs', 'Slider', 'ToolTip', 'AlertBox', 'DialogBox', 'ProgressBar']

    for element in first_step_elements:
        if element.text in text_elements:
            print(element.text, "ok")
        else:
            print("TEST FAILED",element.text, "not in")
            raise NoSuchElementException(f"{element.text} not in text_elements")

def test_first_step_klikanie():
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    first_step_elements = driver.find_elements(By.XPATH, "//li[text()='First Step']//following::li[position()<7]")
    text_elementsF = ['tabs', 'slider', 'tooltip', 'alertbox', 'dialogbox', 'progressbar', ]

    idx = 0
    for _ in first_step_elements:
        # elementy = driver.find_elements(By.XPATH, "//li[text()='First Step']//following::li[position()<7]")
        # actions = ActionChains(driver)
        # elementy[idx].location_once_scrolled_into_view
        # WebDriverWait.until(actions.scroll_to_element(elementy[idx]))
        # actions.move_to_element(elementy[idx]).click().perform()
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_step_elements[idx])
        first_step_elements[idx].click()

        time.sleep(5)
        try:
            driver.switch_to.frame(driver.find_element(By.ID, "aswift_2"))
            driver.switch_to.frame(driver.find_element(By.ID, "ad_iframe"))
            # driver.switch_to.frame(driver.find_element(By.ID, "google_esf"))

            driver.find_element(By.ID, "dismiss-button").click()
            driver.find_element(By.XPATH, "//span[text()='Close']").click()

            driver.find_element(By.XPATH, "//span[@dir='auto']").click()

        except NoSuchElementException:
            print("no start site")
        time.sleep(5)
        current_page_url = driver.current_url
        assert text_elementsF[idx] in current_page_url, f"!!!{text_elementsF[idx]} not in url!!!"
        driver.switch_to.new_window('tab')
        driver.get(url)
        idx+=1

def test_second_step_elements():
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    second_step_elements = driver.find_elements(By.XPATH, "//li[text()='Second Step']//following::li[position()<7]")
    text_elements_second_step = ['Frames', 'Windows', 'Accordion', 'DropDown', 'AutoComplete', 'SelectElements']

    for elemt in second_step_elements:
        if elemt.text in text_elements_second_step:
            print(elemt.text, "ok")
        else:
            print("TEST FAILED",elemt.text, "not in")
            raise NoSuchElementException(f"{elemt.text} not in text_elements")


