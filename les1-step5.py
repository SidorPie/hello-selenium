import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link2 = "http://suninjuly.github.io/find_link_text"
link = "http://suninjuly.github.io/simple_form_find_task.html"
message = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    url = browser.find_element(By.LINK_TEXT, message)
    url.click()
    # browser.get(url.)
    #browser.get(link)

    value1 = "input"
    value2 = "last_name"
    value3 = "city"
    value4 = "country"

    send1 = "Ivan"
    send2 = "Ivanovich"
    send3 = "Ivanovo"
    send4 = "Russia"


    input1 = browser.find_element(By.TAG_NAME, value1)
    input1.send_keys(send1)
    input2 = browser.find_element(By.NAME, value2)
    input2.send_keys(send2)
    input3 = browser.find_element(By.CLASS_NAME, value3)
    input3.send_keys(send3)
    input4 = browser.find_element(By.ID, value4)
    input4.send_keys(send4)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

finally:
    time.sleep(39)
    browser.quit()
