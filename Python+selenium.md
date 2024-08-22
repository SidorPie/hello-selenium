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