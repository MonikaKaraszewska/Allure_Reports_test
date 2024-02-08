from selenium import webdriver
from DemoFirstTest import page_URLs

def test_lambdatest_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(page_URLs.BASE_URL)
    assert driver.title == "LambdaTest Blogs"

def test2_lambdatest_ecommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(page_URLs.ECOMMERCE_URL)
    assert driver.title == "Next-Generation Mobile Apps and Cross Browser Testing Cloud | LambdaTest"

def testRexWebsite():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.rexjones2.com/")
    assert driver.title == "Rex Jones II"