import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Firefox() as browser:
    browser.get(URL)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )


    browser.find_element(By.ID, "book").click()

    x_text = browser.find_element(By.ID, "input_value").text
    y = calc(x_text)
    print(f"{x_text=}")
    print(f"{y=}")
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button#solve").click()

    # Copy returns string
    time.sleep(10)
