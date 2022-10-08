from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 120)
    email = models.CharField(max_length = 120)
    number = models.CharField(max_length = 120)
    text = models.CharField(max_length = 120)
    def __str__(self):
        return self.name