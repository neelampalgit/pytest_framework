import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.config import BASE_URL, USERNAME, PASSWORD


def test_page_load():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    time.sleep(5)
    assert "OrangeHRM" in driver.title, "Page title does not contain OrangeHRM"

    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
    time.sleep(5)

    assert "dashboard" in driver.current_url, "Login failed"

    welcome_text = driver.find_element(By.TAG_NAME, "h6").text
    # assert "Dashboard" in welcome_text, "Dashboard text not found displayed on the dashboard"

    assert driver.find_element(By.ID, "menu_dashboard_index"), "Dashboard menu item not found"
    assert driver.find_element(By.ID, "menu_pim_viewPimModule"), "PIM module not found"