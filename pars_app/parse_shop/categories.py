import requests
from bs4 import BeautifulSoup


main_url = 'https://shop.kz'
headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}



def get_category_url_list() -> list:
    """
    функция возвращает список конечных url, которым будут 
    отправлятся запросы, чтобы получить товары со страницы
    пример:
    https://shop.kz/smartfony/
    https://shop.kz/fitnes-braslety-remeshki/
    https://shop.kz/planshety/
    таких страниц должно получится примерно - 305
    """
    response = requests.get(main_url, headers=headers).text
    catalog_list = []
    soup = BeautifulSoup(response, 'html.parser')
    div_classes = soup.find_all('div', attrs={'class': 'bx-nav-2-lvl-container'})
    for div in div_classes[:-1]:
        urls = div.find_all('li', attrs={'class', 'bx-nav-3-lvl'})
        for url in urls:
            catalog_list.append(main_url + url.find('a').get('href'))
    return catalog_list

