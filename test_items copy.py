from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


try: 
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(3)
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(button) != int(0), \
          f"Not contain add to basket button"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()