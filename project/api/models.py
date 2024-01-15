from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    size = models.IntegerField(verbose_name="Размер")
    manufacturer = models.ForeignKey("Manufacturer", verbose_name="Производитель", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name="Категория", on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name