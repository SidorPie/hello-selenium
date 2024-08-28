Python+selenium
### HTML теги - выписать

## Поиск элементов с помощью CSS-селекторов
- Поиск по id `#bullet`
- Поиск по значению атрибута `[id="bullet"]` вместо `#bullet`
- Поиск по tag 
- Поиск по name `[name="nameValue"]`
- Поиск по class `[class="jumbotron-heading"]` по точному совпадению или .jumbotron-heading - вхождение класса в элемент .lead.text-muted - если несколько классов и порядок не важен

### Использование потомков

`#post2 .title` -  # значит надо искать элемент с id post2, пробел - найти элемент-потомок,  . - элемент-потомок должен иметь класс со значением title. Символ пробела " " в CSS-селекторах разделяет описание предка и потомка. Если `#post2.title` без пробела, то это значит найти элемент, который одновременно содержит id "post2" и класс "title".

### Использование дочерних элементов

`#post2 > div.title` элемент с тегом и классом: div.title, который находится строго на один уровень иерархии ниже чем элемент #post2.

### Использование порядкового номера дочернего элемента
`#posts > .item:nth-child(2) > .title`
Псевдо-класс :nth-child(2) — позволяет найти второй по порядку элемент среди дочерних элементов для #posts. Затем с помощью конструкции > .title указываем, что нам нужен элемент .title, родителем которого является найденный ранее элемент .item

### Использование нескольких классов
`.title.second`

### Примеры
input[required]


## Поиск элементов с помощью XPath

* `el1/el2` — выбирает элементы el2, являющиеся прямыми потомками el1;
* `el1//el2` — выбирает элементы el2, являющиеся потомками el1 любой степени вложенности.
* `//div`
* [] - фильтрация по:
- атрибуту `//img[@id='bullet']`
- по порядковому номеру `//div[@class="row"]/div[2]`
- полному совпадению текста (единственный способ поиска по внутреннему тексту) `//p[text()="Lenin cat"]`
- частичному совпадению `//p[contains(text(), "cat")]`
- логика: `//img[@name='bullet-cat' and @data-type='animal']`
* * - выбор всех элементов `//div/*[@class="jumbotron-heading"]`

### Примеры
'//label[text()="Email*"]/following-sibling::input'
'//div[@class="form-group first_class"]/input')'



## Поиск элементов с помощью Selenium
### find_element()
* By.ID By.CSS_SELECTOR By.XPATH By.NAME By.TAG_NAME By.CLASS_NAME By.LINK_TEXT By.PARTIAL_LINK_TEXT
- browser.close() закрывает текущее окно браузера. если скрипт вызвал всплывающее окно, или открыл что-то в новом окне или вкладке браузера, то закроется только текущее окно, а все остальные останутся висеть.
- browser.quit() закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии.
- https://stackoverflow.com/questions/15067107/difference-between-webdriver-dispose-close-and-quit

### Checkbox and radibutton
тег label рядом с input. Используется, чтобы сделать кликабельным текст, который отображается рядом с флажком. Этот текст заключен внутри тега label. Элемент label связывается с элементом input с помощью атрибута for, в котором указывается значение атрибута id для элемента input:

```html
<div>
  <input type="radio" id="python" name="language" checked>
  <label for="python">Python</label>
</div>
<div>
  <input type="radio" id="java" name="language">
  <label for="java">Java</label>
</div> 
```

### get_attribute()
```python
robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None
```

### Списки
```html
<label for="dropdown">Выберите язык программирования:</label>
	<select id="dropdown" class="custom-select">
	<option selected>--</option>
	<option value="1">Python</option>
	<option value="2">Java</option>
	<option value="3">JavaScript</option>
</select>

```
```python
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
```
### execute_script("JS arguments[]",arg)
```python
browser.execute_script("window.scrollBy(0, 100);")
browser.execute_script("alert('Robots at work');")
browser.execute_script("document.title='Script executing';alert('Robots at work');")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_label_elem)
```

### Загрузка файлов

```python
uploat = browser.find_element(By.CSS_SELECTOR,"#file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'upload.txt')
uploat.send_keys(file_path)
```

### Модальные окна
#### Alert
```python
alert = browser.switch_to.alert
alert.accept()
```
```pyton
alert = browser.switch_to.alert
alert_text = alert.text
```
#### Confirm
```python
confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()
```
#### Prompt
```python
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
```

### Переход на новую вкладку
`browser.switch_to.window(window_name)`
`new_window = browser.window_handles[1]`
`first_window = browser.window_handles[0]`

### Настройка ожиданий
#### Implicit
```python
link = "http://suninjuly.github.io/wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)
```
#### Explicit
```python
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
```
```python
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
	EC.element_to_be_clickable((By.ID, "verify"))
)
```

## Ссылки
https://barancev.github.io/good-locators/
https://www.selenium.dev/documentation/webdriver/waits/
https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
https://www.cloudbees.com/blog/get-selenium-to-wait-for-page-load
https://barancev.github.io/slow-loading-pages/
https://barancev.github.io/page-loading-complete/
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView
https://flukeout.github.io/

#  unittest и PyTest
`assert abs(-42) == 42`
`print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")`

```python
catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"  
```

```python
def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
```

```python
def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, \
        f"expected {expected_result}, got {actual_result}"
```
https://docs.python.org/3/library/unittest.html
### Фиксируем пакеты в requirements.txt 
Создадим виртуальное окружение:`$ python3 -m venv selenium_env`
Активируем окружение: `$ source selenium_env/bin/activate` .bat

`pip freeze > requirements.txt`
`pip install -r requirements.txt`
### pytest commands
https://gist.github.com/amatellanes/12136508b816469678c2

### PyTest фикстурs
фикстуры - декоратор для функций инициализаторов и финализаторов. Могут содержать инициализацию данных или браузера и очистку данных или корректное закрытие. начальные и финальные действия разделяются оператором yield, код после которого выполнится после выполнения теста, использующего эту фикстуру.

`@pytest.fixture(scope="class")` - выполнится один раз для класса. Можно один раз инициализировать браузер для нескольких тестов
`@pytest.fixture(autouse=True)` - выполнится перед каждым тестом
https://habr.com/ru/companies/yandex/articles/242795/
https://docs.pytest.org/en/stable/explanation/fixtures.html


## Маркировка тестов
`@pytest.mark.smoke`
`@pytest.mark.regression`
`pytest -s -v -m smoke test_fixture8.py`
`pytest -s -v -m smoke test_fixture8.py -q --tb=no -p no:warnings`
`pytest -s -v -m "not smoke" test_fixture8.py`
`pytest -s -v -m "smoke or regression" test_fixture8.py`

pytest.ini:
```
[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
```

`@pytest.mark.skip` - пропустить тест при сборе тестов для запуска (то есть не запускать тест) или запустить, но отметить особенным статусом тот тест, который ожидаемо упадёт из-за наличия бага, чтобы он не влиял на результаты прогона всех тестов.
`@pytest.mark.xfail(reason="fixing this bug right now")` - Пока разработчики исправляют баг, мы хотим, чтобы результат прогона всех наших тестов был успешен, но падающий тест помечался соответствующим образом, чтобы про него не забыть. Запуск: `pytest -rx -v test_fixture10a.py`

## конфигурация тестов
conftest.py
```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
```
test_conftest.py
```python
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
```
## Параметризация тестов
`@pytest.mark.parametrize('language', ["ru", "en-gb"])`
https://docs.pytest.org/en/latest/how-to/parametrize.html
Можно параметризовать и класс, тогда во все тестовые функции надо передавать еще и параметр


## Conftest.py и передача параметров в командной строке
Conftest.py
```python
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
```
test_parser.py
```python
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
```
команды запуска 
`pytest -s -v --browser_name=chrome test_parser.py`
`pytest -s -v --browser_name=firefox test_parser.py`

## Плагины и перезапуск тестов
`pip install pytest-rerunfailures`

`pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py`

## Запуск автотестов для разных языков интерфейса


Полезные ссылки
https://stepik.org/lesson/237258/step/1?unit=209646

## Page Object