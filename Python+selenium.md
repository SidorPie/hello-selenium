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