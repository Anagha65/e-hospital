from django.db import models

# Create your models here.

class Facility(models.Model):
    fac_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    resources = models.TextField()

    def __str__(self):
        return '{}'.format(self.fac_name)
