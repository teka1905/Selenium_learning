"""
1. Открыть страницу http://suninjuly.github.io/file_input.html
2. Заполнить текстовые поля: имя, фамилия, email
3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4. Нажать кнопку "Submit""
"""
from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Alexey')
    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Dolmatov')
    email = browser.find_element_by_name('email')
    email.send_keys('teka1905@gmail.com')
    file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    file.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
