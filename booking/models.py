from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    passengers = models.PositiveIntegerField()
    destination = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
