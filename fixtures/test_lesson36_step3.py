import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('page_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, page_id):
    link = f"https://stepik.org/lesson/{page_id}/step/1/"
    browser.get(link)
    text = browser.find_element_by_css_selector('.textarea')
    print('Нашли элемент для ввода текста')
    answer = math.log(int(time.time()))
    print('Отправили ответ', answer)
    text.send_keys(str(answer))
    button = browser.find_element_by_class_name('submit-submission')
    print('Нашли кнопку')
    button.click()
    print('Нажали кнопку')
    message = browser.find_element_by_class_name('smart-hints__hint')
    print('Message text = ', message.text)
    assert 'Correct' in message.text, 'Not "Correct!"'
