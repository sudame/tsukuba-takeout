from django.db import models


class StoreGenre(models.Model):
    name = models.TextField(unique=True)
    slug = models.CharField(unique=True, max_length=24)

    def __str__(self):
        return self.name


class StoreArea(models.Model):
    name = models.TextField(unique=True)
    slug = models.CharField(unique=True, max_length=24)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.TextField(unique=True)
    slug = models.CharField(unique=True, max_length=24)
    genres = models.ManyToManyField(to=StoreGenre)
    address = models.TextField()
    area = models.ForeignKey(to=StoreArea, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    notice = models.TextField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    store = models.ForeignKey(
        to=Store, on_delete=models.CASCADE, related_name="tickets"
    )
    name = models.CharField(max_length=300)
    expire = models.DateField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class StoreOpeningHour(models.Model):
    store = models.ForeignKey(
        to=Store, on_delete=models.CASCADE, related_name="opening_hours"
    )
    opening_time = models.TimeField()
    closing_time = models.TimeField()


class StoreTicketHour(models.Model):
    store = models.ForeignKey(
        to=Store, on_delete=models.CASCADE, related_name="ticket_hours"
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
