import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Firefox() as browser:
    browser.get(url)

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(.5)
    browser.switch_to.window(browser.window_handles[-1])
    time.sleep(.5)
    x_text = browser.find_element(By.ID, "input_value").text
    y = calc(x_text)
    print(f"{x_text=}")
    print(f"{y=}")
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Copy returns string
    time.sleep(10)
