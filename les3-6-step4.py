from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
import pytest

links = ("https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1")

# links = ("https://stepik.org/lesson/236895/step/1")

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', links)
class TestMainPage1():
    def test_login(self, browser, link):
        # Get link
        browser.get(link)
        # Click login
        browser.find_element(By.CSS_SELECTOR,'a[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]').click()
        # Fill login form
        browser.find_element(By.CSS_SELECTOR,'input[name="login"]').send_keys("")
        browser.find_element(By.CSS_SELECTOR,'input[name="password"]').send_keys('')
        browser.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
        time.sleep(3)
        
        answerTextBox = browser.find_element(By.CLASS_NAME,"ember-text-area.ember-view.textarea.string-quiz__textarea")
        isAnswerTextBoxDisabled = answerTextBox.get_attribute("disabled")
        if isAnswerTextBoxDisabled != 'true':
            answer = math.log(int(time.time()))
            answerTextBox.send_keys(answer)
            button = browser.find_element(By.CSS_SELECTOR,'button[class="submit-submission"]')
            button.click()

        hint = browser.find_element(By.CSS_SELECTOR,'p[class="smart-hints__hint"]')
        hintText = hint.text
        assert hintText == "Correct!", \
            f"{hintText}"
