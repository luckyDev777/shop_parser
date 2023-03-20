### Выполненное тестовое задание"

Задание реализовал в виде django приложения <pars_app> внути которого расположена директория parse_shop 
В ней хранится основная логика парсера сайта shop.kz

В файле views.py в контроллере update вызываем функцию pars()
которая даст нам список словерей, далее делается запись в БД sqlite3

<ul>
  <li><b>parse_products.py</b> - Делает запрос на сайт shop.kz и собирает все доступные ссылки которые ведут непосредственно к станицам товара, и далее делает запрос к страницам товаров и достает из страницы максимальное число пагинации, cохраняет данные в categories.json в виде: {url: int(pagin_max)}.
  <li> Запускаем сервер ./manage.py runserver, Далее после сохранения файлов с товарами, надо нажать на ссылку в 
  странице http://127.0.0.1:8000/ который запускает скрипт и записывает данные в базу sqlite.
  Данные можно посмореть в админ панели django</li>
</ul>


### Установка и запуск:


<pre>
$ git clone https://github.com/MansurMekin/shop_parser.git
$ cd shop_parser
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 manage.py migrate

<i>запускаем файл product_total_page.py для получения список 
словарей в формате json</i>
<i>
Словарь будет выглядит примерно так:
{'https://shop.kz/bloki-pitaniya/': 10}
{'https://shop.kz/korpusa/': 9}
{'https://shop.kz/kulery-dlya-protsessora/': 8}
{'https://shop.kz/vodyanoe-okhlazhdenie/': 4}
{'https://shop.kz/termopasta/': 1}
.....
где {"url страницы товара': 'максимальное число страниц'}
</i>
$ python phars_shop/phars_shop/product_total_page.py

<i>Запускаем django, для остановки Ctrl + C</i>
$ ./manage.py runserver 

<i>Открываем http://127.0.0.1:8000/ и видим "привет, для обновления базы нажмите сюда(ссылка)"</i>
<i>после нажатия запускается скрипт парсера parse_products.py</i>

<i>Примерно такие принты будут в терминале:</i>
https://shop.kz/smartfony/?PAGEN_1=8
https://shop.kz/smartfony/?PAGEN_1=9
https://shop.kz/smartfony/?PAGEN_1=10
https://shop.kz/smartfony/?PAGEN_1=11
https://shop.kz/smartfony/?PAGEN_1=12
https://shop.kz/smartfony/?PAGEN_1=13
https://shop.kz/smartfony/?PAGEN_1=14
Finished
https://shop.kz/smart-chasy/?PAGEN_1=1
https://shop.kz/smart-chasy/?PAGEN_1=2
https://shop.kz/smart-chasy/?PAGEN_1=3
https://shop.kz/smart-chasy/?PAGEN_1=4
https://shop.kz/smart-chasy/?PAGEN_1=5
https://shop.kz/smart-chasy/?PAGEN_1=6
        Finished

<i>В каталоге data_json будут храниться файлы json по категориям</i>
<i>После отработки скрипта parse_products.py, надо создать суперпользователя djnago командой</i>
$ python3 manage.py createsuperuser

<i>далее надо зайти в админку django и там увидим записанные данные в БД</i>
</pre>



