from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    year_release = models.IntegerField(verbose_name="Год выпуска")
    country = models.CharField(max_length=30, verbose_name="Страна")
    director = models.ForeignKey("Director", verbose_name="Режиссер", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", verbose_name="Жанр", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Director(models.Model):
    fio = models.CharField(max_length=100, verbose_name="ФИО")
    year = models.IntegerField(verbose_name="Возраст")

    def __str__(self):
        return self.fio


class Genre(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")

    def __str__(self):
        return self.name


class Poster(models.Model):
    date = models.DateField(verbose_name="Дата")
    film = models.ForeignKey("Film", verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.film)
