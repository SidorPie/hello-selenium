from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    h5 = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#price"),"100")
    )
    button = browser.find_element(By.CSS_SELECTOR,"#book")  
    button.click()

     # Получение значения из страницы
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # Ввод значения в форму ответа
    input_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_element.send_keys(y)

    # Клик кнопки погрузки
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    