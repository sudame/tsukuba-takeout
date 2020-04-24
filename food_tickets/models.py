from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="tickets")
    name = models.CharField(max_length=300)
    price = models.IntegerField()

    def __str__(self):
        return self.name
