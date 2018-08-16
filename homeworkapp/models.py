from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    score = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '学生'
