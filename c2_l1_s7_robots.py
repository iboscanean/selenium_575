import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Firefox() as browser:
    browser.get(url)

    x_text = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x_text)
    print(f"{x_text=}")
    print(f"{y=}")
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Copy returns string
    time.sleep(10)
