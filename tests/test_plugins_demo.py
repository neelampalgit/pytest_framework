# 1. pytest-html
# 2. pytest-xdist
# 3. pytest-rerunfailures
# 4. pytest-cov
#***************************************
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.config import BASE_URL


def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(BASE_URL)
    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
    time.sleep(5)

    assert "Dashboard" in driver.page_source

    driver.quit()

@pytest.mark.flaky(reruns=2)
def test_flakiness():
    assert 3==3
