import time

import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
url = "https://www.globalsqa.com/demo-site/"


driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
# first_step_elements = driver.find_elements(By.XPATH, "//li[text()='First Step']//following::li[position()<7]")
# text_elementsF = ['tabs', 'slider', 'tooltip', 'alertBox', 'dialogBox', 'progressBar', ]
idx = 0
# for elem in first_step_elements:
# time.sleep(10)
driver.find_element(By.XPATH, "//a[text()='Tabs']").click()
# time.sleep(10)
try:
    driver.switch_to.frame(driver.find_element(By.ID, "aswift_2"))
    driver.switch_to.frame(driver.find_element(By.ID, "ad_iframe"))
# driver.find_element(By.ID,"dismiss-button").click()
    driver.find_element(By.XPATH, "//span[text()='Close']").click()
except NoSuchElementException:
    print("no start site this time")

driver.get(url)
time.sleep(5)

progressBar = driver.find_element(By.XPATH, "//a[text()='ProgressBar']")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", progressBar)

progressBar.click()
