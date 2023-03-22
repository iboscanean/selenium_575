import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = "http://suninjuly.github.io/selects1.html"


def sum_str(x:str, y:str):
    return str(int(x) + int(y))

with webdriver.Firefox() as browser:
    browser.get(url)

    num1_text = browser.find_element(By.ID, "num1").text
    num2_text = browser.find_element(By.ID, "num2").text
    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select.select_by_visible_text(sum_str(num1_text, num2_text))
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Copy returns string
    time.sleep(10)
