# tests/test_login_with_logging.py
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://opensource-demo.orangehrmlive.com"
USERNAME = "Admin"
PASSWORD = "admin123"

@pytest.fixture(scope="session")
def setup_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_successful_login_with_logging(setup_driver):
    logging.info("Starting the login test for OrangeHRM.")
    driver = setup_driver
    driver.get(BASE_URL)
    logging.info(f"Navigated to {BASE_URL}")

    driver.find_element("name", "username").send_keys(USERNAME)
    logging.info("Entered username.")
    driver.find_element("name", "password").send_keys(PASSWORD)
    logging.info("Entered password.")
    driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
    logging.info("Clicked the login button.")

    assert "dashboard" in driver.current_url.lower(), "Login failed - dashboard not found in URL."
    logging.info("Login successful, reached the dashboard.")
