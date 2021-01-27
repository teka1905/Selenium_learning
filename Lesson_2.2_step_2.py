"""
1. Открыть страницу http://suninjuly.github.io/selects1.html
2. Посчитать сумму заданных чисел
3. Выбрать в выпадающем списке значение равное расчитанной сумме
4. Нажать кнопку "Submit"
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

try:
    number1 = browser.find_element_by_id('num1')
    number11 = number1.text
    number2 = browser.find_element_by_id('num2')
    number22 = number2.text
    number3 = str(int(number11) + int(number22))
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(number3)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(5)
    browser.quit()

