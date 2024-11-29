import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.config import BASE_URL


# @pytest.fixture(params=[("Admin", "admin123"), ("InvalidAdmin", "admin123")])
# def setup_driver(request):
#     username, password = request.param
#     driver = setup_driver
#     driver=webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.get(BASE_URL)
#
#     assert "OrangeHRM" in driver.title, "Page title does not contain OrangeHRM"
#
#     driver.find_element(By.NAME, "username").send_keys(username)
#     driver.find_element(By.NAME, "password").send_keys(password)
#     driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
#     time.sleep(2)
#
#     yield driver
#     driver.quit()

# @pytest.fixture(scope="session")
# def set_driver():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.get(BASE_URL)
#     yield driver
#     driver.quit()
#
# @pytest.fixture
# def login_and_cleanup(set_driver,request):
#     driver = set_driver
#     driver.find_element(By.NAME, "username").send_keys("Admin")
#     driver.find_element(By.NAME, "password").send_keys("admin123")
#     driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
#     time.sleep(2)
#
#     def logout():
#         print("Logging out")
#         driver.quit()
#
#     request.addfinalizer(logout)
#     return driver

# conftest.py
import pytest
import logging

@pytest.fixture(autouse=True, scope="session")
def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
                        handlers=[logging.FileHandler("test_log.log"), logging.StreamHandler()])
    yield
