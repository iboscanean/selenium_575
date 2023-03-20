import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/huge_form.html"

with webdriver.Firefox() as browser:
    browser.get(url)

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("answer")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # Copy returns exec time string
    time.sleep(5)
