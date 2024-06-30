import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestLoginBrowsers():
    @pytest.fixture(params=["firefox", "safari", "chrome"])
    def driver(self, request):
        if request.param == "chrome":
            driver = webdriver.Chrome()
        elif request.param == "firefox":
            driver = webdriver.Firefox()
        elif request.param == "safari":
            driver = webdriver.Safari()

        driver.set_window_size(1512, 867)
        yield driver
        driver.quit()

    def test_login_browsers(self, driver):
        username = os.getenv("PORTAL_USERNAME", "")
        password = os.getenv("PORTAL_PASSWORD", "")
        driver.get("https://portal.aut.ac.ir/")
        time.sleep(3)

        driver.find_element(By.NAME, "sso").click()
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()
        driver.find_element(By.CSS_SELECTOR, "span:nth-child(2)").click()
