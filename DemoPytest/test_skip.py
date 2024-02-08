import sys
from datetime import datetime

import pytest
from selenium import webdriver
import requests

class TestLambdaTest:
    driver = None
    def test_sample_app_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://helion.pl/")
        pytest.skip()
        expected_title  = "Księgarnia informatyczna helion.pl - informatyka w najlepszym wydaniu."
        assert expected_title == self.driver.title
        print(self.driver.title)

    @pytest.mark.skip(reason='Code Has Not been Deployed')
    def test_ecommerce_title(self):
        driver = webdriver.Chrome()
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=17")
        expected_title = "Software"
        assert expected_title == driver.title


    # @pytest.mark.skip()
    def test_special_offers(self):
        driver = webdriver.Chrome()
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/special")
        expected_title = "Special Offers"
        assert expected_title == driver.title


    @pytest.mark.skipif(
        datetime.now() >= datetime(2025,12,31),
        reason="repo is not complete until finishig tutorial")
    def test_pytes_github_repo(self):
        driver = webdriver.Chrome()
        driver.get("https://github.com/RexJonesII/PytestTutorials")
        expected_title = "GitHub - RexJonesII/PytestTutorials: This repository contains source code for Python's Pytest Framework Video Tutorial"
        print(driver.title)
        assert expected_title == driver.title

    @pytest.mark.skipif(sys.version_info < (4, 6), reason="requires python 4.6 or higher")
    def test_sys_version_skip(self):
        driver = webdriver.Chrome()
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/special")
        expected_title = "Special Offers"
        assert expected_title == driver.title

    @pytest.mark.skipif('pandas' not in sys.modules,
                        reason="requires the pandas library")
    def test_pandas_in_skip(self):
        driver = webdriver.Chrome()
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/special")
        expected_title = "Special Offers"
        assert expected_title == driver.title
