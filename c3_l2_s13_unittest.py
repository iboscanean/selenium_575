import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def answer_registration_page(url: str):
    with webdriver.Firefox() as browser:
        browser.implicitly_wait(5)
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, "div.first_block>div.first_class>input.first").send_keys("Firstname")
        browser.find_element(By.CSS_SELECTOR, "div.first_block>div.second_class>input.second").send_keys("Lastname")
        browser.find_element(By.CSS_SELECTOR, "div.first_block>div.third_class>input.third").send_keys("Email")
        browser.find_element(By.CSS_SELECTOR, "div.second_block>div.first_class>input.first").send_keys("Phone")
        browser.find_element(By.CSS_SELECTOR, "div.second_block>div.second_class>input.second").send_keys("Address")
        browser.find_element(By.CSS_SELECTOR, "div.second_block>div.second_class>input.second").send_keys("Address")
        browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()
        h1_tag = browser.find_element(By.TAG_NAME, "h1")

        return h1_tag.text


class TestAbs(unittest.TestCase):

    def test_reg_page_1(self):
        url = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            answer_registration_page(url)
        )

    def test_reg_page_2(self):
        url = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            answer_registration_page(url)
        )


if __name__ == "__main__":
    unittest.main()
