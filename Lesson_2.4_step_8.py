"""
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
browser.implicitly_wait(5)
try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element_by_id('book')
    book.click()
    some_number = browser.find_element_by_id('input_value')
    x = int(some_number.text)
    answer = math.log(abs(12 * math.sin(x)))
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(str(answer))
    button = browser.find_element_by_id("solve")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
