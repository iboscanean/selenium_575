import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://suninjuly.github.io/text_input_task.html"
time.sleep(2)

with webdriver.Firefox() as driver:
    driver.get(url)
    time.sleep(2)

    textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
    time.sleep(2)

    textarea.send_keys("get()")
    time.sleep(2)

    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
    submit_button.click()
