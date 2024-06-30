import os

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def initialize_webdriver():
    driver = webdriver.Chrome()
    return driver

def extract_links(driver, url):
    driver.get(url)
    elements = driver.find_elements(By.TAG_NAME, "a")
    links = [element.get_attribute('href') for element in elements]
    return links

def check_link(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code >= 400:
            return True
    except requests.RequestException:
        return True
    return False

def find_broken_links(driver, url):
    username = os.getenv("PORTAL_USERNAME", "")
    password = os.getenv("PORTAL_PASSWORD", "")
    driver.get("https://portal.aut.ac.ir/")
    driver.set_window_size(1512, 867)
    driver.find_element(By.NAME, "sso").click()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()
    driver.find_element(By.CSS_SELECTOR, "span:nth-child(2)").click()

    links = extract_links(driver, url)
    broken_links = [link for link in links if link and check_link(link)]
    return broken_links

def main():
    url_to_check = "https://portal.aut.ac.ir/aportal/LoginRole.jsp"

    driver = initialize_webdriver()
    broken_links = find_broken_links(driver, url_to_check)
    driver.quit()

    if broken_links:
        print("Broken links found:")
        for link in broken_links:
            print(link)
    else:
        print("No broken links found.")

if __name__ == "__main__":
    main()

