from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class TestRegistration(unittest.TestCase):
    def testRegistration1(self):
        TestRegistration.callLink("http://suninjuly.github.io/registration1.html")

    def testRegistration2(self):
        TestRegistration.callLink("http://suninjuly.github.io/registration2.html")
    
    @staticmethod
    def callLink(link):
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        # Для наглядности
        requiredFirstName = browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
        requiredFirstName.send_keys("111")
        # Падает тут на втором тесте NoSuchElementException
        requiredLastName = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
        requiredLastName.send_keys("111")
        requiredEmail = browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
        requiredEmail.send_keys("111")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "Errew"
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
