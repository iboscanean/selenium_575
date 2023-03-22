import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'requirements.txt')

with webdriver.Firefox() as browser:
    browser.get(url)

    browser.find_element(By.NAME, "firstname").send_keys("Firstname")
    browser.find_element(By.NAME, "lastname").send_keys("Lastname")
    browser.find_element(By.NAME, "email").send_keys("john@email.dom")
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    # Copy returns exec time string
    time.sleep(5)
