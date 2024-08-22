from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input_first_name.send_keys("Dmitry")

    input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input_last_name.send_keys("Selivanov")

    input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input_email.send_keys("DnqFP@example.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(5)

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
