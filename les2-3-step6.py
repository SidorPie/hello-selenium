from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    time.sleep(1)

    new_w = browser.window_handles[1]
    old_w = browser.window_handles[1]
    
    browser.switch_to.window(new_w)

    # Получение значения из страницы
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # Ввод значения в форму ответа
    input_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_element.send_keys(y)

    # Клик кнопки погрузки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    