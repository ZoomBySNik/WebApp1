from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=120, verbose_name="Название компании")
    adress = models.CharField(max_length=120, verbose_name="Адрес компании")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания",
        verbose_name_plural = "Компании"

class Product(models.Model):
    title = models.TextField(max_length=120, verbose_name="Название") #наименование продукта
    description = models.TextField(blank=True, null=True, verbose_name="Описание") #описание продукта
    weight = models.TextField(blank=True, verbose_name="Вес", null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Продукт",
        verbose_name_plural = "Продукты"

class Status(models.Model):
    name = models.CharField(max_length=120, verbose_name="Статус продукта")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус",
        verbose_name_plural = "Статусы"

class ProductInstance(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, null=True)
    inv_number = models.CharField(max_length=120, verbose_name="Инвентарный номер")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Статус продукта")
    due_back = models.DateField(blank=True, null=True, verbose_name="Дата окончания статуса продукта")
    custumer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Заказчик")

    def __str__(self):
        return '%s %s %s' % (self.inv_number, self.product, self.status)

    class Meta:
        verbose_name = "Инвентарный номер",
        verbose_name_plural = "Инвентарные номера"