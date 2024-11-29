import sys
import time

import pytest
from selenium.webdriver.common.by import By

from tests.config import BASE_URL

# @pytest.mark.login
@pytest.mark.skip(reason="Feature not implemented")
def test_login(login_and_cleanup):
    driver = login_and_cleanup
    assert "Dashboard" in driver.page_source

@pytest.mark.dashboard
def test_clickPIM():
    print("PIM is clicked......")

@pytest.mark.skipif(sys.platform=="win32", reason="Test does not work on win32")
def test_non_windows_feature():
    assert 1==1

@pytest.mark.xfail(reason="known defect in the login module")
def test_known_issue_login():
    assert False
