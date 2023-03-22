import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = "https://SunInJuly.github.io/execute_script.html"


with webdriver.Firefox() as browser:
    browser.get(url)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Copy returns string
    time.sleep(10)
