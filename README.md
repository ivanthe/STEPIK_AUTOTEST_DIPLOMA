# STEPIK_AUTOTEST_DIPLOMA
# STEPIK.  Финальный проект по курсу <b>Автоматизация тестирования с помощью Selenium и Python</b>


## :open_book: Задание:

В финальном задании необходимо протестировать работу отдельных страниц тестового интернет магазина <a href="http://selenium1py.pythonanywhere.com/en-gb/"><strong>Oscar Sandbox</strong></a>. При написании кода требуется: 
  1) Тесты должны быть описаны в стиле PageObject. Должны быть создан астрактный класс базовой страницы BasePage, и классы MainPage, ProductPage и LoginPage описывающие сооветствующие страницы и наследующие свойства BasePage.
  2) Создать файл conftest.py. Файл должен содержать фикстуру, в которой реализована возможность выбора одного из доступных языков (en (по умолчанию), ru fr, es, fi, pl и другие) - обязательное требование. Дополнительно в фикстуре реализована возможность запускать тесты в одном из бразеров на выбор Chrome (по умолчанию) или FireFox.
  3) Все локаторы должны быть описаны в отдельном файле locators.py. Внутри файла необходимо создать классы соответствующие классам описывающие страницы. 
  4) Создать файл requirements.txt где будут указаны нужные зависимости и их версии.
  5) Написать тесты для проверки различных сценарием поведения пользователя и/или гостя, и методы в соответствующих классах на каждую из страниц.

## :bulb: Реализованные тесты

:white_check_mark: <b>test_main_page.py</b>  -  ТЕСТЫ ГЛАВНОЙ СТРАНИЦЫ  
1) <b>test_guest_should_see_login_link</b> : гость должен видеть на главной странице ссылку для авторизации или регистрации
2) <b>test_guest_can_go_to_login_page</b> : гость должен переходить на страциу для авторизации или регистрации
3) <b>test_guest_cant_see_product_in_basket_opened_from_main_page</b> : при переходе гостя с главной страницы в корзину, корзина должна быть пустой

:white_check_mark: <b>test_product_page.py</b>  -  ТЕСТЫ СТРАНИЦЫ ТОВАРА
1) <b>test_guest_should_see_login_link_on_product_page</b> : гость должен видеть на странице товара ссылку для авторизации или регистрации
2) <b>test_guest_can_go_to_login_page_from_product_page</b> : гость должен переходить на страницу авторизации или регистрации
3) <b>test_guest_can_add_product_to_basket</b> : гость должен иметь возможность добавлять в корзину товар, В корозину должен добавлять выбранный товар, а также цена указанная на странице товара. Прогон по 10 страницам.
4) <b>test_guest_cant_see_success_message</b> : гость не должен видеть сообщение о добавлении товара, до тех пор пока его не добавит
5) <b>test_guest_cant_see_success_message_after_adding_product_to_basket</b> : негативный тест, проврка отсутствия сообщения о добавлении товара в корзину (по заданию, тест должен пропускаться - помечен через skip)
6) <b>test_message_disappeared_after_adding_product_to_basket</b> : сообщение о добавлении товара в корзину должно исчезать в течении 4х секунд (тест ожидаемо падающий. функция пока не реализовано, помечено XFAIL)
7) <b>test_guest_cant_see_product_in_basket_opened_from_product_page</b> : при переходе в корзину, корзина должна быть пуста, поскольку товар еще не добавлен.

:white_check_mark: <b>TestUserAddToBasketFromProductPage</b>  -  ТЕСТЫ СТРАНИЦЫ ТОВАРА ДЛЯ ЗАРЕГЕСТРИРОВАННОГО ПОЛЬЗОВАТЕЛЯ (помещен в отдельный тестовый класс)
1) <b>setup</b> : создаем нового зарегестрированного пользователя (по условиям задания после теста не требуется выходить из акаунта нового пользователя, акаунт не должен удаляться, использование рандомных адресов (с помощью библиотек random или faker) не требуется, для создания случайного адреса логин генерируем с помощью функции time.time().
2)  <b>test_user_cant_see_success_message</b> : после входа в акаунт, пользователь не должен выдиеть что товар добавлен (товаре еще не добавлен в корзину)
3)  <b>test_user_can_add_product_to_basket</b> : пользователь должен иметь возможность добавлять в корзину товар, В корозину должен добавлять выбранный товар, а также цена указанная на странице товара.


## :hammer_and_wrench: Технологии и инструменты:

  <div>
  <img src="https://raw.githubusercontent.com/ivanthe/ivanthe/dbf5c3a512f324d01ccd394d0d315ff37b4d2412/img/logo/python.svg" title="Python" alt="Python" width="50" height="50"/>&nbsp;   
  <img src="https://github.com/ivanthe/ivanthe/blob/main/img/logo/pycharm.png?raw=true" title="Pycharm" alt="Pycharm" width="50" height="50"/>&nbsp; 
  <img src="https://raw.githubusercontent.com/ivanthe/ivanthe/dbf5c3a512f324d01ccd394d0d315ff37b4d2412/img/logo/pytest.svg" title="Pytest" alt="Pytest" width="50" height="50"/>&nbsp;   
  <img src="https://raw.githubusercontent.com/ivanthe/ivanthe/dbf5c3a512f324d01ccd394d0d315ff37b4d2412/img/logo/selenium.svg" title="Selenium" alt="Selenium" width="50" height="50"/>&nbsp;
 </div>



## :heavy_check_mark: Результаты

1) В файле conftest.py объявляется браузер: 
  - В фикстуре реализовано возможность выбирать один из доступных языков (ru, en, fr, es, fi, pl и другие)
  - Дополнительно в фикстуре реализована возможность запуска одного из двух браузеров Chrome или FireFox (по умолчанию установлен Chrome)
2) Все тесты успешно проходит, кроме ожидаемо падающих и помещченных фикстурой skip и xfail (<b>test_guest_cant_see_success_message_after_adding_product_to_basket</b> и <b>test_message_disappeared_after_adding_product_to_basket</b> соответственно.
3) В каждом тесте предусмотрены соответствующие AssertMessage для идентификации теста в случае если в дальнейшем они будут падать.
4) Тест <b>test_guest_can_add_product_to_basket</b> реализован с параметризацией. В параметры фикстуры добавлены 10 тестовых страниц, одна из которых ожидаемо падает (она помечена с помощью XFAIL)
5) Тесты, предназначенные для финального ревью помечены фикстурой ```@pytest.mark.need_review``` Финальное ревью предполагает проверку следующих тестов
  <br>```test_user_can_add_product_to_basket```
  <br>```test_guest_can_add_product_to_basket```
  <br>```test_guest_cant_see_product_in_basket_opened_from_product_page```
  <br>```test_guest_can_go_to_login_page_from_product_page```


## :computer: Локальный запуск

  1. Склонируйте репозиторий
  2. Запустите тест в командной строке
      - Команда для запуска тестов в рамках превью
        ```
        pytest -v --tb=line --language=en -m need_review test_product_page.py
        ``` 
      - Пример команды запуска (браузер по умолчанию Chrome)    -  выбор языка (--language=<<user_language>>  ,где <b> <<user_language>> </b> может быть ru, en, fr, es, fi, pl и другие)
        ```
        pytest --language=ru test_product_page.py
        ``` 

      - Пример команды запуска с выбором браузера Chrome или FireFox  -  (--browser_name=firefox   или   --browser_name=chrome)
        ```
        pytest --language=fr --browser_name=firefox test_main_page.py
        ```

