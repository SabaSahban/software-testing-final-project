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
        print("hi")
        driver.get("https://portal.aut.ac.ir/")
        print("hi 1")
        driver.find_element(By.NAME, "sso").click()
        print("hi 2")
        driver.find_element(By.ID, "username").send_keys(username)
        print("hi 3")
        driver.find_element(By.ID, "password").send_keys(password)
        print("hi 4")
        driver.find_element(By.NAME, "submit").click()
        print("hi 5")
        driver.find_element(By.CSS_SELECTOR, "span:nth-child(2)").click()
