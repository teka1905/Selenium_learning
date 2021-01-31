"""
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
"""

from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    troll = browser.find_element_by_class_name('trollface.btn.btn-primary')
    troll.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    some_number = browser.find_element_by_id('input_value')
    x = int(some_number.text)
    answer = math.log(abs(12 * math.sin(x)))
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(str(answer))
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()