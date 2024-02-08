import requests
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

from utilities.test_data import TestData


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    global driver
    if request.param == "chrome":
        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        driver = webdriver.Chrome(options=opts)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser:", request.param)

    driver.get(TestData.url1)

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    print("Close Driver")
    driver.close() # zamyka biezace okno przegladarki Zamyka tylko bieżące okno przeglądarki, ale nie zamyka całego procesu przeglądarki. Inne otwarte okna pozostaną aktywne.
    # driver.quit()# zamyka przegladarke Zamyka wszystkie otwarte okna przeglądarki i zwalnia zasoby związane z danym procesem przeglądarki.

