import os
import json
from threading import Thread

import requests
from bs4 import BeautifulSoup


def get_response(url, headers, datas:list):
    print(url)
    response = requests.get(url, headers=headers)                
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', attrs={'class': 'bx_catalog_item'})
    for item in items:
        try:
            product_name = item.find('h4', attrs={'class': 'bx_catalog_item_title_text'}).text
            articul = str(item.find('div', attrs={'class': 'bx_catalog_item_XML_articul'}).text).strip()[9:]
            price = item.find('span', attrs={'class': 'bx-more-price-text'}).text
            category_str = item.find('div', attrs={'class': 'bx_catalog_item_container gtm-impression-product'}).get('data-product')
            data_product = json.loads(category_str)
            category = data_product.get('item_category')
            image_url = ['https:' + item.find('div', attrs={'class': 'item_image_container'}).find('picture').find('img', attrs={'class': 'lazyload'}).get('data-src')]
            data = {
                'name': product_name,
                'articul': articul,
                'price': price,
                'category': category,
                'photo_urls': image_url
            }
            datas.append(data)
        except Exception as e:
            print(f'Произошла ошибка при парсинге товара: {e}\nurl: {url}')
    return datas


def pars():
    headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    query = '?PAGEN_1='
    app_dir = os.path.join('phars_app', 'parse_shop')
    filename = 'categories_short.json'
    datas = []

    with open(os.path.join(os.getcwd(), app_dir, filename), encoding='utf-8') as file:
        categories = json.load(file)

    for category in categories:
        for url, pages in category.items():
            threads = []
            for i in range(1, pages + 1):
                t = Thread(target=get_response, args=(f'{url + query}{i}', headers, datas))
                t.start()
                threads.append(t)

            for t in threads:
                t.join()
            print('\tFinished')
    return datas
