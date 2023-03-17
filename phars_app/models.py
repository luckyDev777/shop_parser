from django.db import models


bnt = {'blank': True, 'null': True}

class Category(models.Model):
    category = models.CharField(max_length=256, unique=True, verbose_name="Категория")

    def __str__(self) -> str:
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название товара")
    articul = models.CharField(max_length=256, verbose_name="Артикул в магазине", **bnt)
    price = models.FloatField(verbose_name="Цена", default=0, **bnt)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория товара", **bnt)
    description = models.TextField(verbose_name="Текст Описания", **bnt)
    photo_urls = models.TextField(verbose_name="Список ссылок фотографий", **bnt)

    def __str__(self) -> str:
        return self.name
