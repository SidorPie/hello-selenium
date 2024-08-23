from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
# import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID,"input_value").text
    res = calc(x)
    inputField = browser.find_element(By.ID,"answer" )
    inputField.send_keys("{}".format(res))
    # Клик чекбокса
    checkbox_label_elem = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_label_elem)
    checkbox_label_elem.click()
    # Клик радиобатона robots rule
    radbuttonRR_label_elem = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radbuttonRR_label_elem)
    radbuttonRR_label_elem.click()
    # Клик кнопки погрузки
    button = browser.find_element(By.TAG_NAME, "button")
    # Scroll to button first
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    