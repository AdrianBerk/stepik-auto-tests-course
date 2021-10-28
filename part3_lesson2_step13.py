import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestText(unittest.TestCase):
    def test_registration1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.first').send_keys("test")
            browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.second').send_keys("test")
            browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.third').send_keys("test")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            self.assertEqual(f'Congratulations! You have successfully registered!', welcome_text, f'{self} not equals to {welcome_text}')
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.first').send_keys("test")
        browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.second').send_keys("test")
        browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.third').send_keys("test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(f'Congratulations! You have successfully registered!', welcome_text,
                         f'{self} not equals to {welcome_text}')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()

