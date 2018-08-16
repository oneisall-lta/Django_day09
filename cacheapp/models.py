from django.db import models


# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '蛋糕'
