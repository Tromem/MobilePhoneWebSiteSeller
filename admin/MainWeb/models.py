from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Seller(models.Model):
    Prise = models.IntegerField(name='Цена')
    Tovar = models.CharField(max_length=100,name= 'Товар')
    Type = models.CharField(max_length=100,name= 'Тип')
    model = models.CharField(max_length=100,name= 'Модель')
    RAM = models.CharField(max_length=100,name= 'Оперативная память')
    SSDMemory = models.CharField(max_length=100,name= 'Память')
    DataRelise = models.DateField()
    SizePhone = models.CharField(max_length=100,name= 'Разрешение телефона')
    keyProduct = models.IntegerField()
    garant = models.CharField(max_length=100,name='Гарантия')
    image = models.ImageField(name='Фото', upload_to="./MainWeb/static/img")
    

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.Tovar

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
class Acess(models.Model):
    
    Tovar = models.CharField(max_length=100,name='Аксесуар')
    Prise = models.IntegerField(name='Цена')

    class Meta:
        verbose_name = "Аксесуар"
        verbose_name_plural = "Аксесуары"

    def __str__(self):
        return self.Tovar

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    


