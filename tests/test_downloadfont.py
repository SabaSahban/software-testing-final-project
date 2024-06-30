import os
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDownloadfont():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def login(self):
    username = os.getenv("PORTAL_USERNAME", "")
    password = os.getenv("PORTAL_PASSWORD", "")
    self.driver.get("https://portal.aut.ac.ir/")
    self.driver.set_window_size(1512, 867)
    self.driver.find_element(By.NAME, "sso").click()
    self.driver.find_element(By.ID, "username").send_keys(username)
    self.driver.find_element(By.ID, "password").send_keys(password)
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(2)").click()
  
  def test_downloadfont(self):
    self.login()

    self.driver.get("https://portal.aut.ac.ir/aportal/LoginRole.jsp")
    self.driver.set_window_size(1512, 867)
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) b").click()
  
