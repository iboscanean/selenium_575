import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Firefox() as browser:
    browser.get(url)

    x_text = browser.find_element(By.ID, "input_value").text
    y = calc(x_text)
    print(f"{x_text=}")
    print(f"{y=}")
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(y)
    # time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()
    # time.sleep(3)
    robots_checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_checkbox)
    browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()
    # time.sleep(3)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Copy returns string
    time.sleep(10)
