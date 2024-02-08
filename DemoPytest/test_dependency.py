import pytest
from selenium import webdriver

class TestLambdaTest:
    driver = None


    def test_dependency_Longman_last(self):
        driver = webdriver.Chrome()
        driver.get("https://www.ldoceonline.com/")
        expected_title = 'Longman Dictionary of Contemporary English | LDOCE'
        assert expected_title == driver.title


    @pytest.mark.dependency()
    def test_dependency_Cambridge(self):
        driver = webdriver.Chrome()
        driver.get("https://dictionary.cambridge.org/")
        expected_title = 'Cambridge Dictionary | English Dictionary, Translations & Thesaurus'
        assert expected_title == driver.title


    @pytest.mark.dependency(depends=["TestLambdaTest::test_dependency_Cambridge"])
    def test_dependency_Eng_inMIND(self):
        driver = webdriver.Chrome()
        driver.get("https://eimciip.cambridge.org/#wordwaiter")
        expected_title = 'Student 9e Welcome Unit'
        assert expected_title == driver.title
