import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/registration2.html"

with webdriver.Firefox() as browser:
    browser.get(url)

    browser.find_element(By.CSS_SELECTOR, "div.first_block>div.first_class>input.first").send_keys("Firstname")
    browser.find_element(By.CSS_SELECTOR, "div.first_block>div.second_class>input.second").send_keys("Lastname")
    browser.find_element(By.CSS_SELECTOR, "div.first_block>div.third_class>input.third").send_keys("Email")
    browser.find_element(By.CSS_SELECTOR, "div.second_block>div.first_class>input.first").send_keys("Phone")
    browser.find_element(By.CSS_SELECTOR, "div.second_block>div.second_class>input.second").send_keys("Address")
    browser.find_element(By.CSS_SELECTOR, "div.second_block>div.second_class>input.second").send_keys("Address")
    browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()
    # Проверяем, что смогли зарегистрироваться ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    # # Copy returns exec time string
    # time.sleep(5)
