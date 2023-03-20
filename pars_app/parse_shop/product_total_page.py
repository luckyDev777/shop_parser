import requests
from bs4 import BeautifulSoup
from categories import get_category_url_list
import json



headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}



def get_total_categories(urls: list) -> list[dict]:
    """фунция получает на вход список urls, который формирует
    функция get_category_url_list(), на выходе получаем список 
    словарей, где словарь должен получиться по типу:
    {url_category: количество доступных пагинации, то есть страниц}
    """
    url_list_with_total = []
    for url in urls:
        response = requests.get(url, headers=headers).content
        soup = BeautifulSoup(response, 'html.parser')
        # time.sleep(1)
        div_classes = soup.find('div', attrs={'class': 'bx-pagination bx-blue'})
        if div_classes:
            pag_span = div_classes.find_all('li')[-2]
            pag_int = pag_span.find('span').text
            print({url: int(pag_int)})
            url_list_with_total.append({url: int(pag_int)})
        else:
            print({url: 1})
            url_list_with_total.append({url: 1})
    return url_list_with_total


url_list = get_category_url_list()
url_list_with_category = get_total_categories(url_list)


# Записываем данные в файл в формате JSON чтоб не отправлять запрос повторно
with open('categories.json', 'w', encoding='utf-8') as file:
    json.dump(url_list_with_category, file, indent=3)


