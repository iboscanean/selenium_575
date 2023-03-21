import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Firefox() as browser:
    browser.get(url)

    x_text = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    y = calc(x_text)
    # print(f"{x_text=}, {y=}")
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # # Copy returns exec time string
    time.sleep(5)
