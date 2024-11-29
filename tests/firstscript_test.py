# Files: Pytest looks for files starting with test_ or ending with _test.py.
# Functions: Each test function should start with test_.
import time

from selenium import webdriver


def test_sample():
    assert 1==1
    print("Test 1 passed")

def test_sample_new():
    assert 1==1

def test_sample_old():
    assert 1==1

def test_open_orangehrm():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    time.sleep(5)
    assert "OrangeHRM" in driver.title
