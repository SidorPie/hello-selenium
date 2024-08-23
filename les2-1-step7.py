from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Получение значения из страницы
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    # Подсчет по формуле

    y = calc(x)
    # Ввод значения в форму ответа
    input_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_element.send_keys(y)
    # Клик чекбокса
    checkbox_label_elem = browser.find_element(By.ID, 'robotCheckbox')
    checkbox_label_elem.click()
    
    # Peoplerule <input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    # Клик радиобатона robots rule
    radbuttonRR_label_elem = browser.find_element(By.ID, 'robotsRule')
    radbuttonRR_label_elem.click()
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
    