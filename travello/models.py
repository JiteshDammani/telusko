from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class DailyRecords(models.Model):
    date = models.DateField()
    transact = models.CharField(max_length=12)
    input = models.CharField(max_length=50)
    rate = models.FloatField()
    quantity = models.IntegerField()
    amount = models.IntegerField()
    remarks = models.CharField(max_length=150)

