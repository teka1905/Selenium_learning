"""
1. Открыть страницу http://SunInJuly.github.io/execute_script.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x.
4. Проскроллить страницу вниз.
5. Ввести ответ в текстовое поле.
6. Выбрать checkbox "I'm the robot".
7. Переключить radiobutton "Robots rule!".
8. Нажать на кнопку "Submit".
"""

from selenium import webdriver
import time
import math

link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    some_number = browser.find_element_by_id('input_value')
    x = int(some_number.text)
    f = str(math.log(abs(12*math.sin(x))))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(f))
    robot = browser.find_element_by_id('robotCheckbox')
    robot.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    robotRule = browser.find_element_by_id('robotsRule')
    robotRule.click()
    button.click()


finally:
    time.sleep(5)
    browser.quit()

