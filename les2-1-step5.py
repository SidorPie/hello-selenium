from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Получение значения из страницы
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    # Подсчет по формуле
    y = calc(x)
    # Ввод значения в форму ответа
    input_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_element.send_keys(y)
    # Клик чекбокса
    checkbox_label_elem = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox_label_elem.click()
    # Клик радиобатона
    radbutton_label_elem = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radbutton_label_elem.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    