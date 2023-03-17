import requests
from bs4 import BeautifulSoup
import json



headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}


query = '?PAGEN_1='


with open('categories.json', encoding='utf-8') as file:
    categories = json.load(file)

all_data = []
data_by_category = {}

with requests.Session() as s:
    for category in categories:
        for url, pages in category.items():
            c = 0
            for i in range(1, pages + 1):
                response = s.get(f'{url + query}{i}', headers=headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                items = soup.find_all('div', attrs={'class': 'bx_catalog_item'})
                for item in items:
                    c += 1
                    try:
                        product_name = item.find('h4', attrs={'class': 'bx_catalog_item_title_text'}).text
                        articul = str(item.find('div', attrs={'class': 'bx_catalog_item_XML_articul'}).text).strip()[9:]
                        price = item.find('span', attrs={'class': 'bx-more-price-text'}).text
                        category_str = item.find('div', attrs={'class': 'bx_catalog_item_container gtm-impression-product'}).get('data-product')
                        data_product = json.loads(category_str)
                        category = data_product.get('item_category')
                        image_url = ['https:' + item.find('div', attrs={'class': 'item_image_container'}).find('picture').find('img', attrs={'class': 'lazyload'}).get('data-src')]
                        print('-'*100)        
                        print(c, f'product_name - {product_name}')
                        print(f'articul - {articul}')
                        print(price)
                        print(category)
                        print(image_url)
                        data = {
                                'name': product_name,
                                'articul': articul,
                                'price': price,
                                'category': category,
                                'photo_urls': image_url
                            }
                        all_data.append(data)
                        if category not in data_by_category:
                            data_by_category[category] = []
                        data_by_category[category].append(data)
                        # Записываем данные в файл в формате JSON
                        with open(f'{category}.json', 'a', encoding='utf-8') as f:
                            json.dump(data, f, ensure_ascii=False, indent=4)
                        print(f'{category} сохранен')
                    except Exception as e:
                        print(f'Произошла ошибка при парсинге товара: {e}')
                    










        





