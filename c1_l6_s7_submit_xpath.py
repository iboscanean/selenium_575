import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/find_xpath_form"

with webdriver.Firefox() as browser:
    browser.get(url)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    # browser.find_element(By.XPATH, "//button[@type='submit']").click()
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()
    # Copy returns exec time string
    time.sleep(5)
