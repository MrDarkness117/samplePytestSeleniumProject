## Документация по работе с фреймворком.

### Структура проекта sampleSeleniumProject:
```
page_objects
tests
conftest.py
paths.py
pytest.ini
selenium_prefs.json
auth_creds.json
```

*conftest.py* – содержит в себе фикстуры для запуска тестов через Pytest.
*paths.py* – содержит в себе пути для загрузки и сохранения файлов
*selenium_prefs.json* – служит для настройки работы браузеров

```
page_objects:
  base:
    base_element.py
    base_page.py
    core_locators.py
    locator.py
  github_auth_page.py
```

page_objects – содержит в себе page objects для различных тестов. Всем page objects необходимо наследовать CoreLocators, что позволяют легко находить элементы через XPath, CLASS_NAME, ID и др. В дальнейшем каждый элемент страницы объявляется как @property и возвращает, например, self.XPATH("<XPATH элемента>"). Все методы для взаимодействия с элементами, в т.ч. проверки (assert/verify) делаются через методы внутри base_element.py
Для демонстрации был создан метод verify_has_text.
В объекты-наследники CoreLocators также необходимо объявлять `__init__` с указанием driver, url (передавать в переменную) и super-класс.

```
tests:
  login_page_tests.py
```
tests – содержит в себе наборы тестов. Запускаются через pytest. Для демонстрации был создан mark "auth". Запускать можно либо через команду `pytest -v -m auth` (тесты авторизации) либо посредством создания bat-файлов с активацией среды (venv) и запуска различных тестов.


### Установка
1. git pull https://github.com/MrDarkness117/samplePytestSeleniumProject.git
2. python3 -m venv virtualenvname (Или создать venv через pycharm)
3. cd ../samplePytestSeleniumProject/venv/Scripts/; activate.bat либо ./activate.ps1 либо activate (если на Linux)
4. pip install -r requirements.txt
5. pytest -v (чтобы убедиться что всё на месте и работает)

### Создание page objects
1. Импортировать CoreLocators по аналогии github_auth_page.py
2. Создать класс (например, SampleClass), наследовать от CoreLocators
3. Создать метод класса (или property), в методе вернуть (return) веб-элемент через любой из инструментов (self.XPATH, self.ID, self.CLASS_NAME)
4. Создание теста
5. Импортировать pytest (import pytest)
6. Импортировать Page object: import PageObject (SampleClass из примера выше) as Page
7. Создать новую функцию теста, в данном случае я не использовал ООП, вместо этого применяю обычные функции для запуска тестов и помечаю их через @pytest.mark.<тип теста>.
8. Сохранить в новую переменную, например, page, сущность Page(driver=fixture_name), в моем примере это page = Page(driver=setup_login)
9. Для перехода на страницу тестирования использовать метод go(): page.go()
10. Описывать дальнейшие шаги тест-кейсов с применением методов page object в base_element, например page.page_webelement_name`.input_text()`, `.click()`, `.hover()` и других. Закончить реализацией методами `.verify`, например есть готовый метод `.verify_has_text("text")`

Дополнительно
- В тестах можно применить logging и помечать дополнительную информацию, например о начале тестирования через `logging.info()`. Файл экспортируется в `test.log`
- Можно использовать `pytest-html` для генерации отчетов. Чтобы сгенерировать отчет нужно в строке запуска pytest указать `--html=../reports/htmlreport.html` (Либо любое другое имя помимо htmlreport), например, `pytest -v -m auth --html=../reports/htmlreport.html`. Файл можно будет найти в папке reports.
- Для ускорения тестов можно применить `pytest-xdist` и передать параметр `-n <кол-во процессоров>`, в данном случае применять более 2-х нет смысла.
