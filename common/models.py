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


class SteamUser(models.Model):
    # TODO: Optimize 'max_length'.
    # Rank of the game.
    rank = models.IntegerField(blank=True)
    # User ID
    steam_ID = models.CharField(max_length=17)
    #
    last_two_weeks = models.FloatField(max_length=500, blank=True)
    #
    ATH = models.FloatField(max_length=10000, blank=True)
    #
    score_sum = models.FloatField(max_length=2, blank=True)
    #
    status_U_count = models.FloatField(max_length=2, blank=True)
    #
    level = models.IntegerField(blank=True)
    #
    badges = models.IntegerField(blank=True)
    #
    games = models.IntegerField(blank=True)
    #
    friends = models.IntegerField(blank=True)
    #
    groups = models.IntegerField(blank=True)
    #
    screenshots = models.IntegerField(blank=True)
    #
    Reviews = models.IntegerField(blank=True)
    #
    Cluster = models.IntegerField(blank=True)
    #
    R = models.FloatField(max_length=10, blank=True)


# Show this DB in Djiango Administration website.
admin.site.register(SteamUser)
