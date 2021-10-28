import logging
import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

logger = logging.getLogger()


def calc():
    return math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.mark.parametrize('link',
                         [
                             'https://stepik.org/lesson/236895/step/1',
                             'https://stepik.org/lesson/236896/step/1',
                             'https://stepik.org/lesson/236897/step/1',
                             'https://stepik.org/lesson/236898/step/1',
                             'https://stepik.org/lesson/236899/step/1',
                             'https://stepik.org/lesson/236903/step/1',
                             'https://stepik.org/lesson/236904/step/1',
                             'https://stepik.org/lesson/236905/step/1]']
                         )
def test_guest_should_see_login_link(browser, link):
    browser.get(f'{link}')
    answer = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
    answer.send_keys(calc())
    button_submit = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
    button_submit.click()
    WebDriverWait(browser, 12).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    smart_hint = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    if smart_hint != 'Correct!':
        logger.info(smart_hint)
    assert smart_hint == 'Correct!', f'{smart_hint}'
