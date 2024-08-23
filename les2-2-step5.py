from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    # Scroll to button first
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # browser.execute_script("alert('Robots at work');")
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    