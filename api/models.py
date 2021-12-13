from django.db import models

# Create your models here.

class Farmers(models.moodel):
    fullname = models.Charfield(max_length=255)
    phone = models.Charfield(max_length=255)
    email = models.Charfield(max_length=255)

    def __str __(self):
        return self.fullname