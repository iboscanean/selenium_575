import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Firefox()
# browser.get(url)
# button = browser.find_element(By.ID, "submit_button")
# time.sleep(3)
# print(button)
# browser.quit()
with webdriver.Firefox() as browser:
    browser.get(url)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    print("done")
