from django.db import models
from django.contrib import admin


# Create your models here.
class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phoneNumber = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)

    # qq
    # Allow Empty string: null=True
    # Allow Empty value : blank=True
    qq = models.CharField(max_length=30, null=True, blank=True)


# Show this DB in Djiango Administration website.
admin.site.register(Customer)
