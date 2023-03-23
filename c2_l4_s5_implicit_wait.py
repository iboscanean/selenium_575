from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://suninjuly.github.io/wait1.html"

with webdriver.Firefox() as browser:
    browser.implicitly_wait(5)

    browser.get(URL)

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text
