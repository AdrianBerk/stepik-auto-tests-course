import os.path
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.NAME, 'firstname').send_keys('xx')
    browser.find_element(By.NAME, 'lastname').send_keys('xx')
    browser.find_element(By.NAME, 'email').send_keys('xx')

    f_element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    f_element.send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()