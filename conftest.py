import pytest
#from data.testdata import *

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome("/Users/akshaykalyanashetti/Downloads/chromedriver")
    driver.get("https://app.saveo.in")
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    # yield
    # driver.quit()