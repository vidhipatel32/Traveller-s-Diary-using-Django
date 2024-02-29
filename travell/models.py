from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=20)
    season = models.CharField(max_length=20)
    duration = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="dest/images/")

    def __str__(self):
        return self.name
