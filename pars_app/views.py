from django.shortcuts import HttpResponse

from pars_app.models import Product, Category

from pars_app.parse_shop.parse_products import pars

def hi(request):
    return HttpResponse('Привет. Для обновления базы нажми <a href="/update">сюда</a>.')

def update(request):
    datas = pars()
    for data in datas:
        category, _ = Category.objects.get_or_create(
            category=data.get('category', 'No Category')
        )
        price = data.get('price', None)
        price = price[:-1].replace(' ', '') if price else price

        product, _ = Product.objects.get_or_create(name=data['name'])
        product.articul = data.get('articul', None)
        product.price = price
        product.category = category
        product.photo_urls = data.get('photo_urls', None)
        product.save()
    return HttpResponse('База обновлена. Нажми <a href="/update">сюда</a> для повторного обновления.')
    
