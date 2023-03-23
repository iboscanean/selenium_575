import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Firefox() as browser:
    browser.get(url)

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(1)
    browser.switch_to.alert.accept()
    time.sleep(1)
    x_text = browser.find_element(By.ID, "input_value").text
    y = calc(x_text)
    print(f"{x_text=}")
    print(f"{y=}")
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Copy returns string
    time.sleep(10)
