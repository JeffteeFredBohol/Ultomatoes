from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    birthdate = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
