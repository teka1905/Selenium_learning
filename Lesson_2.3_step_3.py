"""
1. Открыть страницу http://suninjuly.github.io/alert_accept.html
2. Нажать на кнопку
3. Принять confirm
4. На новой странице решить капчу для роботов, чтобы получить число с ответом
"""

from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    some_number = browser.find_element_by_id('input_value')
    x = int(some_number.text)
    answer = math.log(abs(12*math.sin(x)))
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(str(answer))
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

