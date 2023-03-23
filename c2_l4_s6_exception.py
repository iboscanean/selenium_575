from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://suninjuly.github.io/cats.html"

with webdriver.Firefox() as browser:
    browser.implicitly_wait(5)

    browser.get(URL)

    button = browser.find_element(By.ID, "button")
