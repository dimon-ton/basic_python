from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    detail = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class ContactList(models.Model):
    email = models.CharField(max_length=200)
    head = models.CharField(max_length=200)
    detail = models.CharField(max_length=1000)

    def __str__(self):
        return self.email + ' ' + self.head

